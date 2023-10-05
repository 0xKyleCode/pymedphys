import enum
from typing import List, Literal
from shapely.geometry import Polygon as shapelyPolygon, box
import numpy as np


class MultileafCollimator:
    """
    Class representing a symmetric multileaf collimator
    """

    DEFAULT_LEAF_WIDTHS = np.ones(60)
    DEFAULT_MAX_EXTENSION = 1.5
    DEFAULT_MAX_ADJACENT_OFFSET = 0.5

    LEFT = 0
    RIGHT = 1

    def __init__(
        self,
        leafWidths=None,
        maxLeafExtension=None,
        maxAdjacentOffset=None,
        doLeafClipping=False,
    ):
        """
        Create a symmetric multileaf collimator
        :param leafWidths: list of floats
        :param numLeaves: number of leaves
        :return:
        """

        self.leafWidths = leafWidths or self.DEFAULT_LEAF_WIDTHS
        self.numLeaves = len(self.leafWidths)
        self.maxLeafExt = maxLeafExtension or self.DEFAULT_MAX_EXTENSION
        self.maxAdjOff = maxAdjacentOffset or self.DEFAULT_MAX_ADJACENT_OFFSET
        self.totalLeafWidth = np.sum(self.leafWidths)
        self.useClipping = doLeafClipping

        self._bankPosFunctions = [None, None]
        self._bankInterpPoints = [None, None]
        self._bankInterpVals = [None, None]

        self.leafTop, self.leafMid, self.leafBot = self.calcLeafEdges()

        self._leaves = np.array(
            [[0.0 for s in range(self.numLeaves)], [0.0 for s in range(self.numLeaves)]]
        )

    @property
    def leftBank(self):
        return self._leaves[self.LEFT]

    @property
    def rightBank(self):
        return self._leaves[self.RIGHT]

    def setClipping(self, doClipping):
        self.useClipping = doClipping

    def setLeafBank(self, bankNumber, leafPositions):
        """
        set positions for single bank
        :param bankNumber: int in (self.LEFT, self.RIGHT)
        :param leafPositions: list of leaf positions
        :return:
        """

        assert bankNumber in [self.LEFT, self.RIGHT]

        if self.useClipping:
            leafPositions = self._clipBank(leafPositions)

        if bankNumber == self.LEFT:
            self._checkBankLegality(leafPositions, self.rightBank)
        else:
            self._checkBankLegality(self.leftBank, leafPositions)

        self._leaves[bankNumber] = leafPositions

    def setAperture(self, leftBank, rightBank):
        """
        set both leaf banks simultaneously
        :param leftBank: list of left bank leaf positions
        :param rightBank: list of right bank leaf positions
        :return:
        """

        if self.useClipping:
            leftBank, rightBank = self._clipAperture(leftBank, rightBank)

        self._checkBankLegality(leftBank, rightBank)

        self._leaves[self.LEFT] = leftBank
        self._leaves[self.RIGHT] = rightBank

    def setLeafPosition(self, bankNumber, leafNumber, closedFraction):
        """
        set single leaf position
        :param bankNumber: int L/R bank number in (self.LEFT,self.RIGHT)
        :param leafNumber: int number of leaf
        :param closedFraction: leaf positions in (0, self.maxLeafExt)
        :return:
        """

        assert bankNumber in [self.LEFT, self.RIGHT]
        assert leafNumber < self.numLeaves

        self._leaves[bankNumber][leafNumber] = closedFraction
        self._checkBankLegality(self.leftBank, self.rightBank)

    class IllegalApertureException(Exception):
        pass

    class LeafOverExtendException(IllegalApertureException):
        pass

    class LeafLROverlapException(IllegalApertureException):
        pass

    class LeafMaxAdjacentException(IllegalApertureException):
        pass

    class NegativeLeafPosition(IllegalApertureException):
        pass

    def _checkBankLegality(self, leftBank, rightBank):
        """
        check legality of given left / right bank, raise exception if not legal
        :param leftBank: left bank positions
        :param rightBank: right bank positions
        :return:
        """

        assert len(leftBank) == len(rightBank) == self.numLeaves

        if np.any(leftBank > self.maxLeafExt) or np.any(rightBank > self.maxLeafExt):
            raise self.LeafOverExtendException()

        if np.any(leftBank < 0) or np.any(rightBank < 0):
            raise self.NegativeLeafPosition()

        if np.any(leftBank + rightBank > 2):
            raise self.LeafLROverlapException()

        # FIXME floating point error on subtract leads to difference being exactly adjacent offset, mult by 1.01 to fix
        if np.any(np.abs(np.ediff1d(leftBank)) > 1.01 * self.maxAdjOff) or np.any(
            np.abs(np.ediff1d(rightBank)) > 1.01 * self.maxAdjOff
        ):
            # print leftBank
            # print np.abs(np.ediff1d(leftBank)) > self.maxAdjOff
            # print np.abs(np.ediff1d(leftBank))
            #
            #
            # print "right"
            # print rightBank
            # print np.abs(np.ediff1d(rightBank))

            raise self.LeafMaxAdjacentException

    def calcLeafEdges(self):
        """
        calculate leaf top, middle, bottoms
        :return: (leafTops, leafMids, leafBots)
        """
        topEdge = np.cumsum(self.leafWidths)
        botEdge = topEdge - self.leafWidths
        mid = topEdge - (self.leafWidths / 2.0)
        return topEdge, mid, botEdge

    def applyBankPosFunction(self, bankNumber, posFunc):
        """
        apply function on (0,1) (0,1) to set bank positions
        :param bankNumber: L/R int ident for bank in (self.LEFT,self.RIGHT)
        :param posFunc: function defined on (0,1),(0,1) to apply to bank
        :return:
        """

        leafSpace, posSpace = self._calcNormedFuncXY(posFunc)

        self.setLeafBank(bankNumber, posSpace)

        self._bankPosFunctions[bankNumber] = posFunc

    def applyAperturePosFunction(self, leftFunc, rightFunc):
        lLeafSpace, lPosSpace = self._calcNormedFuncXY(leftFunc)
        rLeafSpace, rPosSpace = self._calcNormedFuncXY(rightFunc)

        self.setAperture(leftBank=lPosSpace, rightBank=rPosSpace)

        self._bankPosFunctions[self.LEFT] = leftFunc
        self._bankPosFunctions[self.RIGHT] = rightFunc

    def applyInterpPointPositions(self, bankNumber, interpPos, interpVal, kind="cubic"):
        """
        calculate a cubic spline and apply function to leaf positions
        :param bankNumber: L/R int in [self.LEFT, self.RIGHT]
        :param interpPos: positions of spline points on [0,1] [normed to (0,self.totalLeafWidth)]
        :param interpVal: value of spline points on [0,1] [normed to (0,self.maxLeafExt)]
        :param kind: type of interpolation passed to scipy.interpolate.interp1d (default 'cubic')
        :return:
        """

        from scipy.interpolate import interp1d

        assert interpPos[0] == 0 and interpPos[-1] == 1
        interpPos = np.array(interpPos)
        interpVal = np.array(interpVal)
        assert np.all(interpVal <= 1) and np.all(interpVal >= 0)

        splFunc = interp1d(interpPos, interpVal, kind=kind)

        self.applyBankPosFunction(bankNumber, splFunc)

        self._bankInterpPoints[bankNumber] = interpPos
        self._bankInterpVals[bankNumber] = self.maxLeafExt * interpVal

    def _calcNormedFuncXY(self, posFunc):
        leafSpace = self.leafMid / self.totalLeafWidth
        posSpace = posFunc(leafSpace) * self.maxLeafExt
        return leafSpace, posSpace

    def getApertureOpening(
        self, numHorizontalVox=100, transmission=None, partial_weighting=False
    ):
        transmission_factor = 0.0
        if transmission is not None:
            assert isinstance(transmission, float)
            opening = np.ones((self.numLeaves, numHorizontalVox)) * transmission
            transmission_factor = transmission
        else:
            opening = np.zeros((self.numLeaves, numHorizontalVox))

        voxSpacing = 2.0 / numHorizontalVox

        # round beamlet positions
        if not partial_weighting:
            left_col = np.rint(self.leftBank / voxSpacing)
            right_col = np.rint((2.0 - self.rightBank) / voxSpacing)

            # slices = []
            for ind, (ls, rs) in enumerate(zip(left_col, right_col)):
                opening[ind, slice(ls, rs)] = 1.0
        # assign partial weights to partially-open beamlets
        else:
            partial_voxel_indices_left = self.leftBank / voxSpacing
            partial_voxel_indices_right = (2.0 - self.rightBank) / voxSpacing

            left_col = np.floor(partial_voxel_indices_left)
            right_col = np.floor(partial_voxel_indices_right)

            for ind, (ls, rs) in enumerate(zip(left_col, right_col)):
                opening[ind, slice(ls, rs)] = 1.0

                pw = 1 - (partial_voxel_indices_left[ind] - ls)
                opening[ind, ls] = max(transmission_factor, pw)

                if rs < numHorizontalVox:
                    pw = partial_voxel_indices_right[ind] - rs
                    opening[ind, rs] = max(transmission_factor, pw)
        return opening

    def plot(self, ax, drawCentroid=True):
        xEdgeBuff = 0.0
        yEdgeBuff = 0.0 * self.totalLeafWidth

        ax.set_xlim(-1 * xEdgeBuff, 2 + xEdgeBuff)
        ax.set_ylim(-1 * yEdgeBuff, self.totalLeafWidth + yEdgeBuff)

        from matplotlib.patches import Rectangle

        top, mid, bot = self.leafTop, self.leafMid, self.leafBot

        for te, xwidth, ywidth in zip(bot, self.leftBank, self.leafWidths):
            ax.add_patch(
                Rectangle(
                    (-1 * xEdgeBuff, te), xwidth + xEdgeBuff, ywidth, fc="blue", ec="k"
                )
            )

        for te, xwidth, ywidth in zip(bot, self.rightBank, self.leafWidths):
            ax.add_patch(
                Rectangle(
                    (2 - xwidth, te), xwidth + xEdgeBuff, ywidth, fc="blue", ec="k"
                )
            )

        ax.add_patch(
            Rectangle(
                (-1 * xEdgeBuff, -1 * yEdgeBuff),
                2 + 2 * xEdgeBuff,
                yEdgeBuff,
                color="black",
            )
        )
        ax.add_patch(
            Rectangle(
                (-1 * xEdgeBuff, self.totalLeafWidth),
                2 + 2 * xEdgeBuff,
                yEdgeBuff,
                color="black",
            )
        )
        ax.add_patch(
            Rectangle(
                (-1 * xEdgeBuff, -1 * yEdgeBuff),
                xEdgeBuff,
                2 * yEdgeBuff + self.totalLeafWidth,
                color="black",
            )
        )
        ax.add_patch(
            Rectangle(
                (2, -1 * yEdgeBuff),
                xEdgeBuff,
                2 * yEdgeBuff + self.totalLeafWidth,
                color="black",
            )
        )

        if self._bankPosFunctions[0] is not None:
            leafSpace, posSpace = self._calcNormedFuncXY(self._bankPosFunctions[0])
            ax.plot(posSpace, leafSpace * self.totalLeafWidth, "-r", lw=3)

        if self._bankPosFunctions[1] is not None:
            leafSpace, posSpace = self._calcNormedFuncXY(self._bankPosFunctions[1])
            ax.plot(2 - posSpace, leafSpace * self.totalLeafWidth, "-r", lw=3)

        if (
            self._bankPosFunctions[0] is not None
            and self._bankPosFunctions[1] is not None
            and drawCentroid
        ):
            lleafSpace, lposSpace = self._calcNormedFuncXY(self._bankPosFunctions[0])
            rleafSpace, rposSpace = self._calcNormedFuncXY(self._bankPosFunctions[1])
            ax.plot(
                (lposSpace + (2 - rposSpace)) / 2.0,
                leafSpace * self.totalLeafWidth,
                "--k",
                lw=1,
            )

        if self._bankInterpPoints[0] is not None:
            ax.plot(
                self._bankInterpVals[0],
                self.totalLeafWidth * self._bankInterpPoints[0],
                "og",
                markersize=10,
            )

        if self._bankInterpPoints[1] is not None:
            ax.plot(
                2 - self._bankInterpVals[1],
                self.totalLeafWidth * self._bankInterpPoints[1],
                "og",
                markersize=10,
            )

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    def _clipBank(self, bank):
        bank[np.where(bank > self.maxLeafExt)] = self.maxLeafExt
        bank[np.where(bank < 0)] = 0.0

        diffs = np.ediff1d(bank)
        absDiff = np.abs(diffs)
        probIndeces = np.where(absDiff > self.maxAdjOff)[0]

        # while problem indeces exist, shave half offset off until adjacent req acheived
        while len(probIndeces) > 0:
            # if there are indeces with adjacent leaves too far out, add/subtract diff
            for ind in probIndeces:
                delta = (absDiff[ind] - self.maxAdjOff) / 2.0

                # FIXME: kludge of 1.01 * delta to avoid float noise on subtraction
                if diffs[ind] < 0:
                    bank[ind] -= 1.01 * delta
                    bank[ind + 1] += 1.01 * delta
                else:
                    bank[ind] += 1.01 * delta
                    bank[ind + 1] -= 1.01 * delta

            diffs = np.ediff1d(bank)
            absDiff = np.abs(diffs)
            probIndeces = np.where(absDiff > self.maxAdjOff)[0]

        return bank

    def _clipAperture(self, leftBank, rightBank):
        leftBank = self._clipBank(leftBank)
        rightBank = self._clipBank(rightBank)

        overInd = np.where(leftBank + rightBank > 2)

        if len(overInd) > 0:
            for ind in overInd:
                delta = np.abs((2 - (leftBank[ind] + rightBank[ind])) / 2.0)
                leftBank[ind] -= delta
                rightBank[ind] -= delta

        return leftBank, rightBank

    def __str__(self):
        toRet = ""
        toRet += "Left Leaves: " + ", ".join([str(f) for f in self._leaves[0]]) + "\n"
        toRet += "Right Leaves: " + ", ".join([str(f) for f in self._leaves[0]]) + "\n"

        return toRet


class MultileafCollimatorISO:
    """
    Class representing a symmetric multileaf collimator
    """

    DEFAULT_LEAF_WIDTHS = np.ones(60)
    DEFAULT_LEAF_HEIGHT = 60

    DEFAULT_MAX_EXTENSION = 1.5
    DEFAULT_MAX_ADJACENT_OFFSET = 10

    LEFT = 0
    RIGHT = 1

    def __init__(
        self,
        leafWidths=None,
        maxLeafExtension=None,
        maxAdjacentOffset=None,
        doLeafClipping=False,
    ):
        """
        Create a symmetric multileaf collimator
        :param leafWidths: list of floats
        :param numLeaves: number of leaves
        :return:
        """

        self.leafWidths = leafWidths or self.DEFAULT_LEAF_WIDTHS
        self.numLeaves = len(self.leafWidths)
        self.maxLeafExt = maxLeafExtension or self.DEFAULT_MAX_EXTENSION
        self.maxAdjOff = maxAdjacentOffset or self.DEFAULT_MAX_ADJACENT_OFFSET
        self.totalLeafWidth = np.sum(self.leafWidths)
        self.useClipping = doLeafClipping

        self._bankPosFunctions = [None, None]
        self._bankInterpPoints = [None, None]
        self._bankInterpVals = [None, None]

        self.leafTop, self.leafMid, self.leafBot = self.calcLeafEdges()

        self._leaves = np.array(
            [[0.0 for s in range(self.numLeaves)], [0.0 for s in range(self.numLeaves)]]
        )

    @property
    def leftBank(self):
        return self._leaves[self.LEFT]

    @property
    def rightBank(self):
        return self._leaves[self.RIGHT]

    def setClipping(self, doClipping):
        self.useClipping = doClipping

    def setLeafBank(self, bankNumber, leafPositions):
        """
        set positions for single bank
        :param bankNumber: int in (self.LEFT, self.RIGHT)
        :param leafPositions: list of leaf positions
        :return:
        """

        assert bankNumber in [self.LEFT, self.RIGHT]

        if self.useClipping:
            leafPositions = self._clipBank(leafPositions)

        if bankNumber == self.LEFT:
            self._checkBankLegality(leafPositions, self.rightBank)
        else:
            self._checkBankLegality(self.leftBank, leafPositions)

        self._leaves[bankNumber] = leafPositions

    def setAperture(self, leftBank, rightBank):
        """
        set both leaf banks simultaneously
        :param leftBank: list of left bank leaf positions
        :param rightBank: list of right bank leaf positions
        :return:
        """

        if self.useClipping:
            leftBank, rightBank = self._clipAperture(leftBank, rightBank)

        self._checkBankLegality(leftBank, rightBank)

        self._leaves[self.LEFT] = leftBank
        self._leaves[self.RIGHT] = rightBank

    def setLeafPosition(self, bankNumber, leafNumber, closedFraction):
        """
        set single leaf position
        :param bankNumber: int L/R bank number in (self.LEFT,self.RIGHT)
        :param leafNumber: int number of leaf
        :param closedFraction: leaf positions in (0, self.maxLeafExt)
        :return:
        """

        assert bankNumber in [self.LEFT, self.RIGHT]
        assert leafNumber < self.numLeaves

        self._leaves[bankNumber][leafNumber] = closedFraction
        self._checkBankLegality(self.leftBank, self.rightBank)

    class IllegalApertureException(Exception):
        pass

    class LeafOverExtendException(IllegalApertureException):
        pass

    class LeafLROverlapException(IllegalApertureException):
        pass

    class LeafMaxAdjacentException(IllegalApertureException):
        pass

    class NegativeLeafPosition(IllegalApertureException):
        pass

    def _checkBankLegality(self, leftBank, rightBank):
        """
        check legality of given left / right bank, raise exception if not legal
        :param leftBank: left bank positions
        :param rightBank: right bank positions
        :return:
        """

        assert len(leftBank) == len(rightBank) == self.numLeaves

        if np.any(leftBank > self.maxLeafExt) or np.any(rightBank > self.maxLeafExt):
            raise self.LeafOverExtendException()

        if np.any(leftBank < 0) or np.any(rightBank < 0):
            raise self.NegativeLeafPosition()

        if np.any(leftBank + rightBank > 2):
            raise self.LeafLROverlapException()

        # FIXME floating point error on subtract leads to difference being exactly adjacent offset, mult by 1.01 to fix
        if np.any(np.abs(np.ediff1d(leftBank)) > 1.01 * self.maxAdjOff) or np.any(
            np.abs(np.ediff1d(rightBank)) > 1.01 * self.maxAdjOff
        ):
            # print "left"
            # print leftBank
            # print np.abs(np.ediff1d(leftBank)) > self.maxAdjOff
            # print np.abs(np.ediff1d(leftBank))
            #
            #
            # print "right"
            # print rightBank
            # print np.abs(np.ediff1d(rightBank)) > self.maxAdjOff
            # print np.abs(np.ediff1d(rightBank))

            raise self.LeafMaxAdjacentException

    def calcLeafEdges(self):
        """
        calculate leaf top, middle, bottoms
        :return: (leafTops, leafMids, leafBots)
        """
        topEdge = np.cumsum(self.leafWidths)
        botEdge = topEdge - self.leafWidths
        mid = topEdge - (self.leafWidths / 2.0)
        return topEdge, mid, botEdge

    def applyBankPosFunction(self, bankNumber, posFunc):
        """
        apply function on (0,1) (0,1) to set bank positions
        :param bankNumber: L/R int ident for bank in (self.LEFT,self.RIGHT)
        :param posFunc: function defined on (0,1),(0,1) to apply to bank
        :return:
        """

        leafSpace, posSpace = self._calcNormedFuncXY(posFunc)

        self.setLeafBank(bankNumber, posSpace)

        self._bankPosFunctions[bankNumber] = posFunc

    def applyAperturePosFunction(self, leftFunc, rightFunc):
        lLeafSpace, lPosSpace = self._calcNormedFuncXY(leftFunc)
        rLeafSpace, rPosSpace = self._calcNormedFuncXY(rightFunc)

        self.setAperture(leftBank=lPosSpace, rightBank=rPosSpace)

        self._bankPosFunctions[self.LEFT] = leftFunc
        self._bankPosFunctions[self.RIGHT] = rightFunc

    def applyInterpPointPositions(self, bankNumber, interpPos, interpVal, kind="cubic"):
        """
        calculate a cubic spline and apply function to leaf positions
        :param bankNumber: L/R int in [self.LEFT, self.RIGHT]
        :param interpPos: positions of spline points on [0,1] [normed to (0,self.totalLeafWidth)]
        :param interpVal: value of spline points on [0,1] [normed to (0,self.maxLeafExt)]
        :param kind: type of interpolation passed to scipy.interpolate.interp1d (default 'cubic')
        :return:
        """

        from scipy.interpolate import interp1d

        assert interpPos[0] == 0 and interpPos[-1] == 1
        interpPos = np.array(interpPos)
        interpVal = np.array(interpVal)
        assert np.all(interpVal <= 1) and np.all(interpVal >= 0)

        splFunc = interp1d(interpPos, interpVal, kind=kind)

        self.applyBankPosFunction(bankNumber, splFunc)

        self._bankInterpPoints[bankNumber] = interpPos
        self._bankInterpVals[bankNumber] = self.maxLeafExt * interpVal

    def _calcNormedFuncXY(self, posFunc):
        leafSpace = self.leafMid / self.totalLeafWidth
        posSpace = posFunc(leafSpace) * self.maxLeafExt
        return leafSpace, posSpace

    def getApertureOpening(
        self, numHorizontalVox=100, transmission=None, partial_weighting=False
    ):
        transmission_factor = 0.0
        if transmission is not None:
            assert isinstance(transmission, float)
            opening = np.ones((self.numLeaves, numHorizontalVox)) * transmission
            transmission_factor = transmission
        else:
            opening = np.zeros((self.numLeaves, numHorizontalVox))

        voxSpacing = 2.0 / numHorizontalVox

        # round beamlet positions
        if not partial_weighting:
            left_col = np.rint(self.leftBank / voxSpacing)
            right_col = np.rint((2.0 - self.rightBank) / voxSpacing)

            # slices = []
            for ind, (ls, rs) in enumerate(zip(left_col, right_col)):
                opening[ind, slice(ls, rs)] = 1.0
        # assign partial weights to partially-open beamlets
        else:
            partial_voxel_indices_left = self.leftBank / voxSpacing
            partial_voxel_indices_right = (2.0 - self.rightBank) / voxSpacing

            left_col = np.floor(partial_voxel_indices_left)
            right_col = np.floor(partial_voxel_indices_right)

            for ind, (ls, rs) in enumerate(zip(left_col, right_col)):
                opening[ind, slice(ls, rs)] = 1.0

                pw = 1 - (partial_voxel_indices_left[ind] - ls)
                opening[ind, ls] = max(transmission_factor, pw)

                if rs < numHorizontalVox:
                    pw = partial_voxel_indices_right[ind] - rs
                    opening[ind, rs] = max(transmission_factor, pw)
        return opening

    def plot(self, ax, drawCentroid=True):
        xEdgeBuff = 0.0
        yEdgeBuff = 0.0 * self.totalLeafWidth

        ax.set_xlim(-1 * xEdgeBuff, 2 + xEdgeBuff)
        ax.set_ylim(-1 * yEdgeBuff, self.totalLeafWidth + yEdgeBuff)

        from matplotlib.patches import Rectangle

        top, mid, bot = self.leafTop, self.leafMid, self.leafBot

        for te, xwidth, ywidth in zip(bot, self.leftBank, self.leafWidths):
            ax.add_patch(
                Rectangle(
                    (-1 * xEdgeBuff, te), xwidth + xEdgeBuff, ywidth, fc="blue", ec="k"
                )
            )

        for te, xwidth, ywidth in zip(bot, self.rightBank, self.leafWidths):
            ax.add_patch(
                Rectangle(
                    (2 - xwidth, te), xwidth + xEdgeBuff, ywidth, fc="blue", ec="k"
                )
            )

        ax.add_patch(
            Rectangle(
                (-1 * xEdgeBuff, -1 * yEdgeBuff),
                2 + 2 * xEdgeBuff,
                yEdgeBuff,
                color="black",
            )
        )
        ax.add_patch(
            Rectangle(
                (-1 * xEdgeBuff, self.totalLeafWidth),
                2 + 2 * xEdgeBuff,
                yEdgeBuff,
                color="black",
            )
        )
        ax.add_patch(
            Rectangle(
                (-1 * xEdgeBuff, -1 * yEdgeBuff),
                xEdgeBuff,
                2 * yEdgeBuff + self.totalLeafWidth,
                color="black",
            )
        )
        ax.add_patch(
            Rectangle(
                (2, -1 * yEdgeBuff),
                xEdgeBuff,
                2 * yEdgeBuff + self.totalLeafWidth,
                color="black",
            )
        )

        if self._bankPosFunctions[0] is not None:
            leafSpace, posSpace = self._calcNormedFuncXY(self._bankPosFunctions[0])
            ax.plot(posSpace, leafSpace * self.totalLeafWidth, "-r", lw=3)

        if self._bankPosFunctions[1] is not None:
            leafSpace, posSpace = self._calcNormedFuncXY(self._bankPosFunctions[1])
            ax.plot(2 - posSpace, leafSpace * self.totalLeafWidth, "-r", lw=3)

        if (
            self._bankPosFunctions[0] is not None
            and self._bankPosFunctions[1] is not None
            and drawCentroid
        ):
            lleafSpace, lposSpace = self._calcNormedFuncXY(self._bankPosFunctions[0])
            rleafSpace, rposSpace = self._calcNormedFuncXY(self._bankPosFunctions[1])
            ax.plot(
                (lposSpace + (2 - rposSpace)) / 2.0,
                leafSpace * self.totalLeafWidth,
                "--k",
                lw=1,
            )

        if self._bankInterpPoints[0] is not None:
            ax.plot(
                self._bankInterpVals[0],
                self.totalLeafWidth * self._bankInterpPoints[0],
                "og",
                markersize=10,
            )

        if self._bankInterpPoints[1] is not None:
            ax.plot(
                2 - self._bankInterpVals[1],
                self.totalLeafWidth * self._bankInterpPoints[1],
                "og",
                markersize=10,
            )

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    def _clipBank(self, bank):
        bank[np.where(bank > self.maxLeafExt)] = self.maxLeafExt
        bank[np.where(bank < 0)] = 0.0

        diffs = np.ediff1d(bank)
        absDiff = np.abs(diffs)
        probIndeces = np.where(absDiff > self.maxAdjOff)[0]

        # while problem indeces exist, shave half offset off until adjacent req acheived
        while len(probIndeces) > 0:
            # if there are indeces with adjacent leaves too far out, add/subtract diff
            for ind in probIndeces:
                delta = (absDiff[ind] - self.maxAdjOff) / 2.0

                # FIXME: kludge of 1.01 * delta to avoid float noise on subtraction
                if diffs[ind] < 0:
                    bank[ind] -= 1.01 * delta
                    bank[ind + 1] += 1.01 * delta
                else:
                    bank[ind] += 1.01 * delta
                    bank[ind + 1] -= 1.01 * delta

            diffs = np.ediff1d(bank)
            absDiff = np.abs(diffs)
            probIndeces = np.where(absDiff > self.maxAdjOff)[0]

        return bank

    def _clipAperture(self, leftBank, rightBank):
        leftBank = self._clipBank(leftBank)
        rightBank = self._clipBank(rightBank)

        overInd = np.where(leftBank + rightBank > 2)

        if len(overInd) > 0:
            for ind in overInd:
                delta = np.abs((2 - (leftBank[ind] + rightBank[ind])) / 2.0)
                leftBank[ind] -= delta
                rightBank[ind] -= delta

        return leftBank, rightBank

    def __str__(self):
        toRet = ""
        toRet += "Left Leaves: " + ", ".join([str(f) for f in self._leaves[0]]) + "\n"
        toRet += "Right Leaves: " + ", ".join([str(f) for f in self._leaves[0]]) + "\n"

        return toRet


class BeamAperture:
    JAW_ISO_LIMIT_X_MM = 400.0
    JAW_ISO_LIMIT_Y_MM = 400.0

    class JAW(enum.Enum):
        Y1 = "Y1"
        X1 = "X1"
        X2 = "X2"
        Y2 = "Y2"

    def __init__(
        self,
        xjaw_settings: List[float],
        yjaw_settings: List[float],
        collimator_angle_degrees: float,
        sid_mm: float,
        sid_mm_iso: float = 1000.0,
    ):
        self.xjaw_settings = xjaw_settings
        self.yjaw_settings = yjaw_settings
        self.collimator_angle_degrees = collimator_angle_degrees
        self.sid_mm = sid_mm
        self.sid_mm_iso = sid_mm_iso

    def get_jaw_setting(self, jaw_id: JAW):
        mag = self.sid_mm_iso / self.sid_mm

        if jaw_id == self.JAW.X1:
            return self.xjaw_settings[0] * mag
        elif jaw_id == self.JAW.X2:
            return self.xjaw_settings[1] * mag
        elif jaw_id == self.JAW.Y1:
            return self.yjaw_settings[0] * mag
        elif jaw_id == self.JAW.Y2:
            return self.yjaw_settings[1] * mag
        else:
            raise ValueError(f"Unknown jaw id: {jaw_id}")

    def get_corners(self, sid_mm: float, iso_sid: float = 1000.0):
        """
        Get the corners of the beam aperture in the DICOM coordinate system for a given SID
        :param sid_mm:  Source to image distance in mm
        :param iso_sid:  The iso SID in mm
        :return: returns the corners of the beam aperture in the DICOM coordinate system
        """
        return (
            self.calc_jaw_bounds_yx(
                self.JAW.X1,
                self.xjaw_settings[0],
                sid_mm,
                self.collimator_angle_degrees,
                iso_sid,
            ),
            self.calc_jaw_bounds_yx(
                self.JAW.X2,
                self.xjaw_settings[1],
                sid_mm,
                self.collimator_angle_degrees,
                iso_sid,
            ),
            self.calc_jaw_bounds_yx(
                self.JAW.Y1,
                self.yjaw_settings[0],
                sid_mm,
                self.collimator_angle_degrees,
                iso_sid,
            ),
            self.calc_jaw_bounds_yx(
                self.JAW.Y2,
                self.yjaw_settings[1],
                sid_mm,
                self.collimator_angle_degrees,
                iso_sid,
            ),
        )

    @property
    def collimator_angle_radians(self):
        return np.deg2rad(self.collimator_angle_degrees)

    @classmethod
    def calc_xjaw_center(
        cls,
        xjaw_setting: float,
        sid_mm: float,
        col_angle_degrees: float = 0.0,
        iso_sid=1000.0,
    ):
        return xjaw_setting * (sid_mm / iso_sid)
        # return cls.rotate_points_yx([0,xjaw_setting * (sid_mm / iso_sid)], col_angle_degrees)[1]

    @classmethod
    def calc_yjaw_center(
        cls, yjaw_setting, sid_mm, col_angle_degrees: float = 0.0, iso_sid=1000.0
    ):
        return yjaw_setting * (sid_mm / iso_sid)
        # return cls.rotate_points_yx([yjaw_setting * (sid_mm / iso_sid),0],col_angle_degrees)[0]

    def calc_jaw_center(
        cls,
        jaw_id: Literal[JAW.X1, JAW.X2, JAW.Y1, JAW.Y2],
        jaw_setting: float,
        sid_mm: float,
        col_angle_degrees: float,
        iso_sid: float = 1000.0,
    ):
        jawPos = jaw_setting * (sid_mm / iso_sid)

        # col0 config

        if jaw_id == cls.JAW.X1:
            jawPos = [0, jawPos]
        elif jaw_id == cls.JAW.X2:
            jawPos = [0, jawPos]
        elif jaw_id == cls.JAW.Y1:
            jawPos = [-1 * jawPos, 0]
        else:
            jawPos = [-1 * jawPos, 0]

        jawPos = cls.rotate_points_yx(jawPos, col_angle_degrees)

        return jawPos

    @classmethod
    def calc_jaw_bounds_yx(
        cls,
        jaw_id: Literal[JAW.X1, JAW.X2, JAW.Y1, JAW.Y2],
        jaw_setting: float,
        sid_mm: float,
        col_angle_degrees: float,
        iso_sid: float = 1000.0,
    ):
        if jaw_id not in [cls.JAW.X1, cls.JAW.Y1, cls.JAW.X2, cls.JAW.Y2]:
            raise ValueError(f"Invalid jaw_id: {jaw_id}")

        jaw_cent = jaw_setting

        if jaw_id == cls.JAW.X1:
            jaw_bound_yx = [
                -1 * cls.JAW_ISO_LIMIT_Y_MM / 2.0,
                cls.JAW_ISO_LIMIT_Y_MM / 2.0,
                jaw_cent - cls.JAW_ISO_LIMIT_X_MM / 2.0,
                jaw_cent,
            ]
        elif jaw_id == cls.JAW.X2:
            jaw_bound_yx = [
                -1 * cls.JAW_ISO_LIMIT_Y_MM / 2.0,
                cls.JAW_ISO_LIMIT_Y_MM / 2.0,
                jaw_cent,
                cls.JAW_ISO_LIMIT_X_MM / 2.0 + jaw_cent,
            ]
        elif jaw_id == cls.JAW.Y1:
            jaw_bound_yx = [
                -1 * jaw_cent,
                -1 * jaw_cent + cls.JAW_ISO_LIMIT_Y_MM / 2.0,
                -1 * cls.JAW_ISO_LIMIT_X_MM / 2.0,
                cls.JAW_ISO_LIMIT_X_MM / 2.0,
            ]
        else:
            jaw_bound_yx = [
                -1 * jaw_cent,
                -1 * cls.JAW_ISO_LIMIT_Y_MM / 2.0 - jaw_cent,
                -1 * cls.JAW_ISO_LIMIT_X_MM / 2.0,
                cls.JAW_ISO_LIMIT_X_MM / 2.0,
            ]

        return jaw_bound_yx

    @classmethod
    def calc_jaw_corners_yx(
        cls,
        jaw_id: Literal[JAW.X1, JAW.X2, JAW.Y1, JAW.Y2],
        jaw_setting: float,
        sid_mm: float,
        col_angle_degrees: float,
        iso_sid: float = 1000.0,
    ):
        print("\t", jaw_id.name, jaw_setting)
        jaw_bound_yx = cls.calc_jaw_bounds_yx(
            jaw_id, jaw_setting, sid_mm, col_angle_degrees, iso_sid
        )

        corners = cls.corners_from_bounds_yx(jaw_bound_yx)

        return cls.rotate_points_yx(corners, col_angle_degrees)

    @classmethod
    def corners_from_bounds_yx(cls, jaw_bounds):
        y1, y2, x1, x2 = jaw_bounds
        return np.array([[y1, x1], [y1, x2], [y2, x2], [y2, x1]])

    @classmethod
    def rotate_points_yx(cls, points, angle_degrees):
        angle_radians = np.deg2rad(angle_degrees)
        rotation_matrix = np.array(
            [
                [np.cos(angle_radians), np.sin(angle_radians)],
                [-1 * np.sin(angle_radians), np.cos(angle_radians)],
            ]
        )
        return np.matmul(points, rotation_matrix)

    def plot_projection(
        self,
        ax,
        sid_mm,
        patch_face_args=dict(edgecolor="blue", facecolor="None", alpha=0.3),
    ):
        for jaw_id in BeamAperture.JAW:
            corners = self.calc_jaw_corners_yx(
                jaw_id,
                self.get_jaw_setting(jaw_id),
                sid_mm,
                self.collimator_angle_degrees,
            )
            corners = [[c[1], c[0]] for c in corners]

            from matplotlib.patches import Polygon as mplPolygon

            polygon = shapelyPolygon(corners)

            xlim = ax.get_xlim()
            ylim = ax.get_ylim()

            clip_rect = box(xlim[0], ylim[0], xlim[1], ylim[1])

            intersected_polygon = polygon.intersection(clip_rect)
            # center_x, center_y = intersected_polygon.centroid.x, intersected_polygon.centroid.y
            mpl_intersected_polygon = mplPolygon(
                list(intersected_polygon.exterior.coords), **patch_face_args
            )
            mpl_intersected_polygon.set_hatch("/")

            jawCentPos = self.JawCenterImage(jaw_id)

            ax.add_patch(mpl_intersected_polygon)
            ax.text(
                jawCentPos[1],
                jawCentPos[0],
                jaw_id.name,
                ha="center",
                va="center",
                fontsize=10,
                color="red",
            )

            ax.plot(self.JawCentralPointYX[1], self.JawCentralPointYX[0], "r+")

    @property
    def X1Image(self):
        return self.JawCenterImage(self.JAW.X1)

    @property
    def X2Image(self):
        return self.JawCenterImage(self.JAW.X2)

    @property
    def Y1Image(self):
        return self.JawCenterImage(self.JAW.Y1)

    @property
    def Y2Image(self):
        return self.JawCenterImage(self.JAW.Y2)

    @property
    def JawCentralPointYX(self):
        jaw_points = [self.X1Image, self.X2Image, self.Y1Image, self.Y2Image]
        return [
            np.mean([s[0] for s in jaw_points]),
            np.mean([s[1] for s in jaw_points]),
        ]

    def JawCenterImage(self, jaw_id: Literal[JAW.X1, JAW.X2, JAW.Y1, JAW.Y2]):
        mag = self.sid_mm / self.sid_mm_iso

        jawPos = self.get_jaw_setting(jaw_id)
        ymid = (
            self.get_jaw_setting(self.JAW.Y1) + self.get_jaw_setting(self.JAW.Y2)
        ) / 2.0
        xmid = (
            self.get_jaw_setting(self.JAW.X1) + self.get_jaw_setting(self.JAW.X2)
        ) / 2.0

        if jaw_id == self.JAW.X1 or jaw_id == self.JAW.X2:
            jawPos = [-1 * ymid, jawPos]
        else:
            jawPos = [-1 * jawPos, xmid]

        jawPos = self.rotate_points_yx(jawPos, self.collimator_angle_degrees)

        return jawPos

        jc = self.calc_jaw_center(
            jaw_id,
            self.get_jaw_setting(jaw_id),
            self.sid_mm,
            self.collimator_angle_degrees,
            self.sid_mm_iso,
        )

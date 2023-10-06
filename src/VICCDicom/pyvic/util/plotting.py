import matplotlib.pyplot as plt
from typing import Optional


def plot_box(
    ax: plt.Axes,
    xlow: float,
    xhigh: float,
    ylow: float,
    yhigh: float,
    fmt: str = "--k",
    **plot_args
) -> None:
    """
    Plot a rectangular box on the provided axis.

    Parameters:
    - ax (plt.Axes): The axis on which to plot.
    - xlow (float): The x-coordinate of the box's left edge.
    - xhigh (float): The x-coordinate of the box's right edge.
    - ylow (float): The y-coordinate of the box's bottom edge.
    - yhigh (float): The y-coordinate of the box's top edge.
    - fmt (str, optional): The format string for plotting. Default is '--k' (dashed black line).
    - **plot_args: Additional keyword arguments to be passed to the plotting function.

    Returns:
    - None: This function modifies the provided axis in-place and does not return any value.

    Example:
    ```
    fig, ax = plt.subplots()
    plot_box(ax, 1, 3, 1, 4, fmt='--r', linewidth=2)
    plt.show()
    ```
    """

    # Get current axis limits
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()

    # Plot the box's four edges
    ax.plot([xlow, xlow], [ylow, yhigh], fmt, **plot_args)
    ax.plot([xhigh, xhigh], [ylow, yhigh], fmt, **plot_args)
    ax.plot([xlow, xhigh], [ylow, ylow], fmt, **plot_args)
    ax.plot([xlow, xhigh], [yhigh, yhigh], fmt, **plot_args)

    # Reset the axis limits
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)


def plot_vertical_line(
    ax: plt.Axes,
    xpos: float,
    fmt: str = "--k",
    label: Optional[str] = None,
    **plot_args
) -> None:
    """
    Plots a vertical line on the provided Axes at the specified x-position.

    Args:
        ax (plt.Axes): Matplotlib Axes on which the vertical line will be plotted.
        xpos (float): X-coordinate at which the vertical line will be plotted.
        fmt (str, optional): Format string for the vertical line. Defaults to '--k'.
        label (Optional[str], optional): Label for the vertical line. If provided, it will be displayed at the bottom of the line. Defaults to None.
        **plot_args: Additional arguments passed to ax.plot().

    Returns:
        None: The function modifies the provided Axes in place.
    """

    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()

    ax.plot([xpos, xpos], [y0, y1], fmt, **plot_args)
    if label:
        ax.text(
            xpos,
            y0,
            label,
            verticalalignment="top",
            horizontalalignment="center",
            fontsize=10,
        )

    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)


def plot_horizontal_line(
    ax: plt.Axes, ypos: float, fmt: str = "--k", **plot_args
) -> None:
    """
    Plots a horizontal line on the provided Axes at the specified y-position.

    Args:
        ax (plt.Axes): Matplotlib Axes on which the horizontal line will be plotted.
        ypos (float): Y-coordinate at which the horizontal line will be plotted.
        fmt (str, optional): Format string for the horizontal line. Defaults to '--k'.
        **plot_args: Additional arguments passed to ax.plot().

    Returns:
        None: The function modifies the provided Axes in place.
    """

    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()

    ax.plot([x0, x1], [ypos, ypos], fmt, **plot_args)

    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)

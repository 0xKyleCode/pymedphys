class BCCALinac:
    """
    A class to represent a BCCA linac.

    Methods
    -------
    get_machine_name(machine: str) -> str
        Returns the machine name.
    get_machine_list() -> list[str]
        Returns a list of all machine names.
    get_machine_model(machine: str) -> str
        Returns the machine model.
    get_machine_hd(machine: str) -> bool
        Returns the machine HD status.
    """

    MACHINES = {
        "fir": {
            "short_name": "fir",
            "long_name": "VIFIR_TB1",
            "model": "TrueBeam",
            "hd": False,
            "id": 1,
        },
        "arbutus": {
            "short_name": "arbutus",
            "long_name": "VIARBUTUS_TB2",
            "model": "TrueBeam",
            "hd": False,
            "id": 2,
        },
        "birch": {
            "short_name": "birch",
            "long_name": "VIBIRCH_TB3",
            "model": "TrueBeam",
            "hd": False,
            "id": 3,
        },
        "cedar": {
            "short_name": "cedar",
            "long_name": "VICEDAR_TB4",
            "model": "TrueBeam",
            "hd": False,
            "id": 4,
        },
        "spruce": {
            "short_name": "spruce",
            "long_name": "VISPRUCE_TB5",
            "model": "TrueBeam",
            "hd": False,
            "id": 5,
        },
        "oak": {
            "short_name": "oak",
            "long_name": "VIOAK_TB6",
            "model": "TrueBeam",
            "hd": True,
            "id": 6,
        },
    }

    @classmethod
    def get_machine_info(cls, machine: str) -> dict:
        """
            Gets a machine's info.

        Args:
            machine (str): The machine name.
        Returns:
            dict: The machine info.
        """
        return cls.MACHINES[machine]

    @classmethod
    def get_machine_name(cls, machine: str) -> str:
        """
        Returns the machine name.

        Args:
            machine (str): Name of the machine

        Raises:
            RuntimeError: If the machine name is not recognized.

        Returns:
            str: The machine name.
        """
        for inner_machine in cls.MACHINES.keys():
            if machine == inner_machine:
                return cls.MACHINES[machine]["name"]
            elif machine == cls.MACHINES[inner_machine]["name"]:
                return cls.MACHINES[inner_machine]["name"]
            else:
                raise RuntimeError("Machine %s not recognized." % machine)

    @classmethod
    def get_machine_list(cls) -> list[str]:
        """
        Returns a list of all machine names.

        Returns:
            list: A list of all machine names.
        """
        return list(cls.MACHINES.keys())

    @classmethod
    def get_machine_model(cls, machine: str) -> bool:
        """
        Returns the machine model.

        Args:
            machine (str): Name of the machine

        Raises:
            RuntimeError: If the machine name is not recognized.

        Returns:
            str: The machine model.
        """
        for inner_machine in cls.MACHINES.keys():
            if machine == inner_machine:
                return cls.MACHINES[machine]["model"]
            elif machine == cls.MACHINES[inner_machine]["name"]:
                return cls.MACHINES[inner_machine]["model"]
            else:
                raise RuntimeError("Machine %s not recognized." % machine)

    @classmethod
    def get_machine_hd(cls, machine: str) -> bool:
        """
        Returns the machine HD status.

        Args:
            machine (str): Name of the machine

        Raises:
            RuntimeError: If the machine name is not recognized.

        Returns:
            bool: The machine HD status.
        """
        for inner_machine in cls.MACHINES.keys():
            if machine == inner_machine:
                return cls.MACHINES[machine]["hd"]
            elif machine == cls.MACHINES[inner_machine]["name"]:
                return cls.MACHINES[inner_machine]["hd"]
            else:
                raise RuntimeError("Machine %s not recognized." % machine)

    @classmethod
    def get_machine_id(cls, machine: str) -> int:
        """_summary_

        Args:
            machine (str): _description_

        Returns:
            int: _description_
        """
        for inner_machine in cls.MACHINES.keys():
            if machine == inner_machine:
                return cls.MACHINES[machine]["id"]
            elif machine == cls.MACHINES[inner_machine]["name"]:
                return cls.MACHINES[inner_machine]["id"]
            else:
                raise RuntimeError("Machine %s not recognized." % machine)

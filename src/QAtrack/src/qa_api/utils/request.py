import requests
from qa_api.utils.dotenv import load_dotenv_to_config
from qa_api.constants.qatrack_constants import settings

root = settings["root"]
config = load_dotenv_to_config(settings["config_file"])


def setup_header() -> dict[str, str]:
    """
    Setup header for QATrack+ API

    Returns:
        dict[str, str]: header for QATrack+ API
    """
    token_url = root + "/get-token/"
    resp = requests.post(
        token_url, data={"username": config["USERNAME"], "password": config["PASSWORD"]}
    )
    token = resp.json()["token"]
    headers = {"Authorization": "Token %s" % token}
    return headers


def get(url: str, params: dict = None) -> dict:
    """

    Get from QATrack+ API

    Args:
        url (str): link to grab from
        params (dict, optional): Optional params. Defaults to None.

    Returns:
        dict: json response
    """
    header = setup_header()
    return requests.get(root + url, params=params, headers=header).json()


def post(url: str, data: dict = None) -> dict:
    """


    Args:
        url (str): _description_
        data (dict, optional): _description_. Defaults to None.

    Returns:
        dict: _description_
    """
    header = setup_header()
    return requests.post(root + url, json=data, headers=header)

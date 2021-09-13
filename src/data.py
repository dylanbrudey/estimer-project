"""Check, then process the data that we retrieve from the API response"""
from requests import Response
import re


def check_response_validity(response: Response) -> bool:
    """
    Check the response validity, whether one has been retrieved, and if it's not an error one
    :param response: response from the api, contains the data
    :return: Indicate if the response is valid and we can process the data from it or not
    """
    if response:
        # The response indicate the request didn't succeed
        if response.status_code in [403, 404, 500]:
            return False
        else:
            return True
    # The response hasn't been retrieved at all
    else:
        return False


def process_data(response: Response) -> tuple:
    """
    Process the response content in order to retrieve the data we are interested in
    :param response: Valid response from the api
    :return: tuple of the data we want to display: the username, the email and emoji of the os
    """
    content: dict = response.json()
    # Store the date we are interested in
    username: str = content['username']
    adresse_email: str = content['email']
    user_agent: str = content['user_agent']
    os_emoji: str = None

    # Check in user_agent the OS used by the user and store in os_emoji the corresponding emoji
    if re.search(r'Windows', user_agent):
        os_emoji = ":window:"
    elif re.search(r'Linux', user_agent):
        os_emoji = ":penguin:"
    # Look for an iOS or MacOs operating system
    elif re.search(r'Mac OS X', user_agent):
        os_emoji = ":red_apple:"
    elif re.search(r'Android', user_agent):
        os_emoji = ":robot:"
    return username, adresse_email, os_emoji

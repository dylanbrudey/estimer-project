""""""
from requests import Response
import re

def checkResponseValidity(response: Response):
    # The response hasn
    if not response:
        pass


def processResponse(response: Response):
    content: dict = response.json()
    username: str = content['username']
    adresse_email: str = content['email']
    user_agent: str = content['user_agent']
    os_emoji: str = None
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

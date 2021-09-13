import emoji
import requests
import json
import re
from request import getData
from data import processResponse
from display import display

print("\U0001FA9F")
print("\N{winking face}")
print(emoji.emojize('python is awesome :window:'))
print(emoji.emojize('python is awesome :penguin:'))
print(emoji.emojize('python is awesome :red_apple:'))
print(emoji.emojize('python is awesome :robot:'))


# def getUserAndDisplay():
#     # requête
#     response = requests.get("https://random-data-api.com/api/internet_stuff/random_internet_stuff")
#     # if none : check si la reqûete à l'api a abouti
#     content: dict = response.json()
#     username: str = content['username']
#     adresse_email: str = content['email']
#     user_agent: str = content['user_agent']
#     os_emoji: str = None
#     if re.search(r'Windows', user_agent):
#         os_emoji = ":window:"
#     elif re.search(r'Linux', user_agent):
#         os_emoji = ":penguin:"
#     # Look for an iOS or MacOs operating system
#     elif re.search(r'Mac OS X', user_agent):
#         os_emoji = ":red_apple:"
#     elif re.search(r'Android', user_agent):
#         os_emoji = ":robot:"
#     # json = json.dumps(content)
#     print(content)
#     print(emoji.emojize("L'adresse email de l'utilisateur {} est {}. Iel utilise le système d'exploitation {}"
#                         .format(username, adresse_email, os_emoji)))
#     if os_emoji == ":robot:":
#         print("Android !")
#     elif not os_emoji:
#         print("Noo no nooooo")


def run():
    response = getData()
    #TODO: reconstruction, déconstruction du tuple
    username, adresse_email, os_emoji = processResponse(response)
    display(username, adresse_email, os_emoji)
# while True:
#     getUserAndDisplay()


if __name__ == "__main__":
    run()
    # getUserAndDisplay()
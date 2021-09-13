""""""
import requests


def getData():
    # requête
    try:
        response = requests.get("https://random-data-api.com/api/internet_stuff/random_internet_stuff")
    except ConnectionError as connectionError:
        print("Problème de connexion : en voici les détails")
        # connectionError.
    finally:
        pass
    # if none : check si la reqûete à l'api a abouti
    return response

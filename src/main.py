"""Program that fetches some user data (username, email, os from user_agent) from an API (
random-data-api) and show the later in the console"""
from requests import Response
from request import make_request
from data import process_data, check_response_validity
from display import display


def run() -> None:
    """
    Run the program step by step
    """
    response: Response = make_request()
    # Process and display the data only if the response is valid
    if check_response_validity(response):
        data: tuple = process_data(response)
        display(data[0], data[1], data[2])
    else:
        print("Une erreur est survenue: impossible de récupérer les données de l'api")


if __name__ == "__main__":
    run()

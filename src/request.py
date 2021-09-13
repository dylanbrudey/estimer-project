"""Make the requests to retrieve the selected response with the contents we are looking for"""

from requests import Response, get
from requests.exceptions import ConnectionError
from constant import api_url


def make_request() -> Response:
    """
    Send a request to the api in order to retrieve the selected response with the contents we are looking for
    :return: Response object of the request with the contents
    """
    response = None
    try:
        response = get(api_url)
    except ConnectionError as connectionError:
        print("Problème de connexion : en voici les détails:\n")
        print("{} \n".format(connectionError.args))
    finally:
        pass
    # if none : check si la reqûete à l'api a abouti
    return response

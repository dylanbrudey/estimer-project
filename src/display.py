"""Display the data retrieved from the api"""
import emoji


def display(username: str, adresse_email: str, os_emoji: str) -> None:
    """
    Display the data from an user retrived from the api
    :param username: username of the user
    :param adresse_email: email of the user
    :param os_emoji: emoji corresponding to the os used by the user
    """
    print(emoji.emojize("\nL'adresse email de l'utilisateur {} est {}. Iel utilise le système d'exploitation {}"
                        .format(username, adresse_email, os_emoji)))

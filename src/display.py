""""""
import emoji


def display(username: str, adresse_email: str, os_emoji: str):
    print(emoji.emojize("L'adresse email de l'utilisateur {} est {}. Iel utilise le système d'exploitation {}"
                        .format(username, adresse_email, os_emoji)))

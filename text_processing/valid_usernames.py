def valid_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def username_containing(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(username):
    if " " in username:
        return False
    return True


def username_is_valid(username):
    if valid_length(username) and username_containing(username) and no_redundant_symbols(username):
        return True
    return False


usernames = input().split(", ")

for username in usernames:
    if username_is_valid(username):
        print(username)

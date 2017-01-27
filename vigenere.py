from helpers import rotate_character, alphabet_position, user_input_is_valid, is_int
from sys import argv


def encrypt(text, key):
    import string
    result = ""
    idx = 0
    for char in text:
        result += rotate_character(char, alphabet_position(key[idx]))
        if char in string.ascii_letters:
            idx = (idx + 1) % len(key)
    return result


def main(message, key):
    return encrypt(message, key)


if __name__ == '__main__':
    if user_input_is_valid(argv):
        main(input("Type a message:\n"), argv[1])

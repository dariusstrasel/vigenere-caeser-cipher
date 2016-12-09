from sys import argv, exit

def alphabet_position(letter):
    import string
    alphabet = string.ascii_letters
    for i in range(0, len(alphabet)):
        if alphabet[i] == letter:
            return i

def rotate_character(char, rot):
    import string
    upper = string.ascii_uppercase
    if char not in string.ascii_letters:
        return char
    if char in upper:
        return string.ascii_uppercase[(alphabet_position(char) + rot) % 26]
    return string.ascii_lowercase[(alphabet_position(char) + rot) % 26]

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def user_input_is_valid(cl_args, enforce_word, enforce_digit):
    if len(cl_args) < 2:
        print("Argument is missing.")
        exit()
    if enforce_word == True:
        if is_int(argv[1]) == True:
            print("Key argument must be a word.")
            exit()
    if enforce_digit == True:
        if is_int(argv[1]) == False:
            print("Key argument must be a digit.")
            exit()
    return True
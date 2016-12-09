test_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

def counting(text_input):
    import string
    alphabet = string.ascii_lowercase
    result = {}
    for item in text_input:
        result[item] = 0
    for item in text_input:
        if item in alphabet:
            result[item] += 1
    print(result)

def get_initials(fullname):
    result = ""
    list = fullname.split(" ")
    for i in list:
        result += i[0].upper()
    return result

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
        #print(alphabet_position(char) + rot % 26)
        return string.ascii_uppercase[(alphabet_position(char) + rot) % 26]
    #print(alphabet_position(char) + rot % 26)
    return string.ascii_lowercase[(alphabet_position(char) + rot) % 26]

def encrypt(text, rot):
    result = ""
    for i in text:
        result += rotate_character(i, rot)
        return result

def caeser(text, rot):
    result = ""
    for i in text:
        result += rotate_character(i, rot)
        return result

def vigenere(text, key):
    result = ""
    idx = 0
    for char in text:
        result += rotate_character(char, alphabet_position(key[idx]))
        idx = (idx + 1) % len(key)
    return result

print(vigenere("pizzapizza","pizzapie"))

#print(len(string.ascii_letters))
#print(rotate_character("Z", 2))
print(alphabet_position("d"))
#print(encrypt("Hello, World!", 5))
# print(counting(test_text))
#print(get_initials("Darius Strasel"))




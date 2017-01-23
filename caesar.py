def alphabet_position(letter):
    """Get rotation value for the letter"""
    if letter.isalpha():
        return ord(letter.lower()) - 97
    else:
        print ('Invalid input for encryption key')
        exit()

def rotate_character(char, rot):
    """Encrypt each character by integer rot"""
    cipher = ''
    if ord(char) < 97:
        cipher = chr(((alphabet_position(char) + rot) % 26) + 65)
    else:
        cipher = chr(((alphabet_position(char) + rot) % 26) + 97)
    return cipher

def encrypt(mess, rot):
    """Use Caesar Encryption to encrypt the message"""
    rot = int(rot)
    cipherText = ''
    for c in mess:
        if c.isalpha():
            cipherText += rotate_character(c, rot)
        else:
            cipherText += c
    return cipherText

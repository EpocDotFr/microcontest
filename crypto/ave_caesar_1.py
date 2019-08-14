# encrypt() and decrypt() functions taken from https://teachen.info/cspp/unit4/lab04-02.html (was too lazy)

from microcontest import Communicator


def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: # if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result


def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: # if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

mc = Communicator.create_from_env()

challenge_id = 4

variables = mc.get_contest_variables(challenge_id)

txt_clair = decrypt(int(variables['key']), variables['txt_crypte'])

data = {'txt_clair': txt_clair}

print(mc.validate_contest(challenge_id, data))

# rle_encode() and rle_decode() functions taken from https://stackabuse.com/run-length-encoding/ (was too lazy)

from microcontest import Communicator


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char

            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char

        return encoding


def rle_decode(data):
    decode = ''
    count = ''

    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * int(count)
            count = ''

    return decode

mc = Communicator.create_from_env()

challenge_id = 31

variables = mc.get_contest_variables(challenge_id)

data = {'resultat_compression': rle_encode(variables['donnees_a_compresser']), 'resultat_decompression': rle_decode(variables['donnees_a_decompresser'])}

print(mc.validate_contest(challenge_id, data))

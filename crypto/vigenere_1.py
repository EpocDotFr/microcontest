# pip install pycipher

from microcontest import Communicator
from pycipher import Vigenere

mc = Communicator.create_from_env()

challenge_id = 10

variables = mc.get_contest_variables(challenge_id)

txt_clair = Vigenere(variables['clef']).decipher(variables['txt_crypte'])

print(txt_clair)

data = {'txt_clair': txt_clair}

print(mc.validate_contest(challenge_id, data))

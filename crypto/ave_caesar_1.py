# pip install pycipher

from microcontest import Communicator
from pycipher import Caesar

mc = Communicator.create_from_env()

challenge_id = 4

variables = mc.get_contest_variables(challenge_id)

txt_clair = Caesar(int(variables['key'])).decipher(variables['txt_crypte'])

data = {'txt_clair': txt_clair}

print(mc.validate_contest(challenge_id, data))

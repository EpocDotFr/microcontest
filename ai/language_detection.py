# pip install langdetect

from microcontest import Communicator
import langdetect

mc = Communicator.create_from_env()

challenge_id = 37

variables = mc.get_contest_variables(challenge_id)

lang1 = langdetect.detect(variables['txt1'])
lang2 = langdetect.detect(variables['txt2'])
lang3 = langdetect.detect(variables['txt3'])
lang4 = langdetect.detect(variables['txt4'])

data = {'lang1': lang1, 'lang2': lang2, 'lang3': lang3, 'lang4': lang4}

print(mc.validate_contest(challenge_id, data))

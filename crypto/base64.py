from microcontest import Communicator
import base64

mc = Communicator.create_from_env()

challenge_id = 50

variables = mc.get_contest_variables(challenge_id)

big_number = int(base64.b64decode(variables['big_number']).decode('ascii'))
half_big_number = base64.b64encode(bytes(str(int(big_number / 2)), 'ascii')).decode('ascii')

data = {'half_big_number': half_big_number}

print(mc.validate_contest(challenge_id, data))

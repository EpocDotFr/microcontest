import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from libmc import mc
import base64

challenge_id = 50

variables = mc.get_contest_variables(challenge_id)

big_number = int(base64.b64decode(variables['big_number']).decode('ascii'))

data = {'half_big_number': base64.b64encode(bytes(str(int(big_number / 2)), 'ascii')).decode('ascii')}

print(mc.validate_contest(challenge_id, data))

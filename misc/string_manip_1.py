import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from libmc import mc

challenge_id = 42

variables = mc.get_contest_variables(challenge_id)

data = {'s3': variables['s1'] + variables['s2']}

print(mc.validate_contest(challenge_id, data))

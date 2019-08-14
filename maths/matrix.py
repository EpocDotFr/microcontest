# pip install numpy

from microcontest import Communicator
import numpy as np

mc = Communicator.create_from_env()

challenge_id = 12

variables = mc.get_contest_variables(challenge_id)

a = np.array(eval(variables['A'].replace('][', '],[')))
b = np.array(eval(variables['B'].replace('][', '],[')))

m = np.linalg.inv(np.dot(a, np.transpose(b)))

m = repr(m).replace(' ', '').replace('array(', '').replace(']])', ']]').replace('\n', '').replace('],[', '][')

data = {'M': m}

print(mc.validate_contest(challenge_id, data))

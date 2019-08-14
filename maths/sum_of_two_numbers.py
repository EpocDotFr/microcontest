from microcontest import Communicator

mc = Communicator.create_from_env()

challenge_id = 1

variables = mc.get_contest_variables(challenge_id)

a = int(variables['a'])
b = int(variables['b'])
s = a + b

data = {'s': s}

print(mc.validate_contest(challenge_id, data))

from microcontest import Communicator

mc = Communicator.create_from_env()

challenge_id = 43

variables = mc.get_contest_variables(challenge_id)

data = {'s_rev': variables['s'][::-1]}

print(mc.validate_contest(challenge_id, data))

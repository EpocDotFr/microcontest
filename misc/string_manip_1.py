from microcontest import Communicator

mc = Communicator.create_from_env()

challenge_id = 42

variables = mc.get_contest_variables(challenge_id)

data = {'s3': variables['s1'] + variables['s2']}

print(mc.validate_contest(challenge_id, data))

from microcontest import Communicator

mc = Communicator.create_from_env()

challenge_id = 14

variables = mc.get_contest_variables(challenge_id)

naissance = int(variables['naissance'])
date_courante = int(variables['date_courante'])
age = date_courante - naissance

data = {'age': age}

print(mc.validate_contest(challenge_id, data))

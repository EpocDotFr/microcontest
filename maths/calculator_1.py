from microcontest import Communicator

mc = Communicator.create_from_env()

challenge_id = 19

variables = mc.get_contest_variables(challenge_id)

result = eval(variables['expr'])

data = {'result': round(result)}

print(mc.validate_contest(challenge_id, data))

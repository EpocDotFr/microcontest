from microcontest import Communicator

mc = Communicator.create_from_env()

challenge_id = 53

variables = mc.get_contest_variables(challenge_id)

mass = int(variables['mass'])
height = int(variables['height'])
sex = int(variables['sex'])
age = int(variables['age'])

bmi = mass / pow(height / 100, 2)
bfp = (1.2 * bmi) + (0.23 * age) - (10.8 * sex) - 5.4

data = {'bmi': round(bmi, 3), 'bfp': round(bfp, 3)}

print(mc.validate_contest(challenge_id, data))

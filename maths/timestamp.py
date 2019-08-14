# pip install pendulum

from microcontest import Communicator
import pendulum

mc = Communicator.create_from_env()

challenge_id = 18

variables = mc.get_contest_variables(challenge_id)

date = pendulum.from_format(variables['date'], 'DD/MM/YYYY HH:mm:ss', tz='Europe/Paris')

data = {'timestamp': date.int_timestamp}

print(mc.validate_contest(challenge_id, data))

from microcontest import Communicator

mc = Communicator.create_from_env()

challenge_id = 23

variables = mc.get_contest_variables(challenge_id)

date = int(variables['date'])
msec = float(variables['msec'])

sat1lat = float(variables['sat1lat'])
sat2lat = float(variables['sat2lat'])
sat3lat = float(variables['sat3lat'])

sat1long = float(variables['sat1long'])
sat2long = float(variables['sat2long'])
sat3long = float(variables['sat3long'])

date1 = int(variables['date1'])
date2 = int(variables['date2'])
date3 = int(variables['date3'])

msec1 = float(variables['msec1'])
msec2 = float(variables['msec2'])
msec3 = float(variables['msec3'])

# data = {'latitude' : latitude, 'longitude': longitude}

# print(mc.validate_contest(challenge_id, data))

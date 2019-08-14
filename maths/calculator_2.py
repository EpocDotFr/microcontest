from math import cos, sin, tan, acos as arccos, asin as arcsin, atan as arctan, cosh, sinh, tanh, acosh as argch, asinh as argsh, atanh as argth, exp, log as ln, log10 as log, sqrt, modf
from microcontest import Communicator


def E(x):
    return modf(x)[1]


def D(x):
    return modf(x)[0]


def calc(expression):
    return eval(expression.replace('_', '-'))

mc = Communicator.create_from_env()

challenge_id = 24

variables = mc.get_contest_variables(challenge_id)

evaluation1 = calc(variables['expression1'])
evaluation2 = calc(variables['expression2'])
evaluation3 = calc(variables['expression3'])

data = {'evaluation1': evaluation1, 'evaluation2': evaluation2, 'evaluation3': evaluation3}

print(mc.validate_contest(challenge_id, data))

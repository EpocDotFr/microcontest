# A* implementation taken from https://www.redblobgames.com/pathfinding/a-star/implementation.html#python (was too lazy)

from microcontest import Communicator

mc = Communicator.create_from_env()

challenge_id = 17

variables = mc.get_contest_variables(challenge_id)

laby = variables['laby']
nb_colonnes = int(variables['nb_colonnes'])
nb_lignes = int(variables['nb_lignes'])
colonne_depart = int(variables['colonne_depart'])
ligne_depart = int(variables['ligne_depart'])
colonne_arrivee = int(variables['colonne_arrivee'])
ligne_arrivee = int(variables['ligne_arrivee'])

chemin = ''

data = {'chemin': chemin}

print(mc.validate_contest(challenge_id, data))

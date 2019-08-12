from configparser import ConfigParser
from dotenv import load_dotenv
from hashlib import sha1
import requests
import os

requests = requests.Session()


class MicroContest:
    CONTEST_VARIABLES_URL = 'http://www.microcontest.com/contests/{contest_id}/contest.php'
    CONTEST_VALIDATION_URL = 'http://www.microcontest.com/contests/{contest_id}/validation.php'

    def __init__(self, username, password):
        self.username = username
        self.password = sha1(password.encode()).hexdigest()

    def get_contest_variables(self, contest_id):
        data = {
            'username': self.username,
            'password': self.password,
            'ID': contest_id,
            'contestlogin': 1,
            'version': 2
        }

        response = requests.post(self.CONTEST_VARIABLES_URL.format(contest_id=contest_id), data=data)

        response.raise_for_status()

        if response.text.startswith('Erreur'):
            raise ValueError(response.text.replace('<br/>', ''))

        response_parser = ConfigParser()
        response_parser.read_string('\n'.join(response.text.replace('<br/>', '\n').splitlines()[1:]))

        return {variable_name: response_parser[variable_name]['Valeur'] for variable_name in response_parser if variable_name != 'DEFAULT'}

    def validate_contest(self, contest_id, data):
        response = requests.post(self.CONTEST_VALIDATION_URL.format(contest_id=contest_id), data=data)

        response.raise_for_status()

        return response.text.splitlines()[0].split(':', maxsplit=1)[1] == '1'

load_dotenv()

mc = MicroContest(os.getenv('MC_USERNAME'), os.getenv('MC_PASSWORD'))

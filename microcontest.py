from dotenv import load_dotenv
from hashlib import sha1
import requests
import os

requests = requests.Session()


class MicroContestError(Exception):
    pass


class Communicator:
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

        response = self._send_request(self.CONTEST_VARIABLES_URL.format(contest_id=contest_id), data)

        return self._parse_contest_variables(response)

    def validate_contest(self, contest_id, data):
        response = self._send_request(self.CONTEST_VALIDATION_URL.format(contest_id=contest_id), data)

        return response.text.splitlines()[0].split(':', maxsplit=1)[1] == '1'

    def _parse_contest_variables(self, response):
        variables = {}

        current_variable_name = None

        for data in response.text.split('<br/>'):
            if not data:
                continue
            elif data.startswith('[') and data.endswith(']'):
                current_variable_name = data.strip('[]')
            elif data.startswith('Valeur'):
                variables[current_variable_name] = data.split('=', maxsplit=1)[1]

                current_variable_name = None

        return variables

    def _send_request(self, url, data):
        response = requests.post(url, data=data)

        response.raise_for_status()

        if response.text.startswith('Erreur'):
            raise MicroContestError(response.text.replace('<br/>', ''))

        return response

    @classmethod
    def create_from_env(cls):
        load_dotenv()

        return cls(os.getenv('MC_USERNAME'), os.getenv('MC_PASSWORD'))

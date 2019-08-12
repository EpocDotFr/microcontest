import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from libmc import mc
from lxml import html
import requests

challenge_id = 44

variables = mc.get_contest_variables(challenge_id)

username = variables['username']

response = requests.get('http://www.wechall.net/en/profile/{}'.format(username))

response.raise_for_status()

parsed = html.fromstring(response.text)

score = int(parsed.xpath('/html/body/div[1]/div[5]/div[1]/table/tr[2]/td/a')[0].text)
rank = int(parsed.xpath('/html/body/div[1]/div[5]/div[1]/table/tr[3]/td/a')[0].text)
register_date = parsed.xpath('/html/body/div[1]/div[5]/div[1]/table/tr[4]/td')[0].text
last_activity = parsed.xpath('/html/body/div[1]/div[5]/div[1]/table/tr[5]/td')[0].text

data = {'score': score, 'rank': rank, 'register_date': register_date, 'last_activity': last_activity}

print(mc.validate_contest(challenge_id, data))

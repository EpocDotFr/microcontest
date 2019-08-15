# pip install pyzbar pillow

from microcontest import Communicator
from pyzbar.pyzbar import decode
from io import BytesIO
from PIL import Image

mc = Communicator.create_from_env()

challenge_id = 39

variables = mc.get_contest_variables(challenge_id)

image_raw = BytesIO(variables['img'].encode())

results = decode(Image.open(image_raw).convert('RGB'))

if results:
    result_data = results[0].data.decode()
    number1, number2 = result_data.split('-', maxsplit=1)

    data = {'number1': number1, 'number2': number2}

    print(mc.validate_contest(challenge_id, data))
else:
    print('No results')

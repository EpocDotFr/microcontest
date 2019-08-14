from microcontest import Communicator
from io import BytesIO
from PIL import Image
import base64

mc = Communicator.create_from_env()

challenge_id = 56

variables = mc.get_contest_variables(challenge_id)

image_raw = BytesIO(base64.b64decode(variables['img_b64']))

image = Image.open(image_raw).convert('RGB')

r, g, b = image.getpixel((1, 1))

data = {'r': r, 'g': g, 'b': b}

print(mc.validate_contest(challenge_id, data))

import requests
from PIL import Image
import os


def get_bond_image(token_id):
    image_dir = os.getcwd() + "/images/"
    cbond_image = str(token_id) + ".png"
    token_image = "https://img.syncbond.com/bond/" + cbond_image
    print("link to cbond image: " + token_image)
    request = requests.get(token_image, stream=True)
    if request.status_code == 200:
        bond = image_dir + cbond_image
        with open(bond, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        bond = Image.open(bond)
        # bond = bond.resize((1024, 512), Image.ANTIALIAS)
        bond = bond.resize((1000, 707), Image.ANTIALIAS)
        bond.save(image_dir + "final_" + cbond_image)
    return image_dir + "final_" + cbond_image

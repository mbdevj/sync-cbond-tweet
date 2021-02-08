import requests



def get_bond_image(token_id):
    bond_image = str(token_id) + ".png"
    token_image = "https://img.syncbond.com/bond/" + bond_image
    print("link to cbond image: " + token_image)
    request = requests.get(token_image, stream=True)
    if request.status_code == 200:
        bond_image = "images/" + bond_image
        with open(bond_image, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    return bond_image

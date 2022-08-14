import scrython
import requests
import time

query = input("Name a card: ")
auto = ""

IMAGE_SAVE_PATH = "./Card Images"


def save_image(path, image_url, file_name):
    response = requests.get(image_url)

    with open('{}/{}.png'.format(path, file_name), 'wb') as file:
        file.write(response.content)


try:
    time.sleep(0.05)
    card = scrython.cards.Named(exact=query)
except Exception:
    time.sleep(0.05)
    auto = scrython.cards.Autocomplete(q=query, query=query)

if auto:
    print("Did you mean?")
    for item in auto.data():
        print(item)
else:
    print(card.name())
    print(card.rarity() + " from " + card.set_name())
    print(card.mana_cost())
    print(card.oracle_text())
    save_image(IMAGE_SAVE_PATH, card.image_uris(0, 'normal'), card.name())

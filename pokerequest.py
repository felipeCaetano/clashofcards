import requests


def hows_pokemon(poke_num):
    request = requests.get(
        f'https://ex.traction.one/pokedex/pokemon/{poke_num}')
    info = dict(request.json()[0])
    print(info['number'])
    print(info['name'])
    print(info['species'])
    print(info['types'])
    print(info['baseStats'])
    print(info['sprite'])
    return (info['number'], info['name'], info['species'], info['types'],
            info['baseStats'], info['sprite'])


if __name__ == '__main__':
    hows_pokemon(135)

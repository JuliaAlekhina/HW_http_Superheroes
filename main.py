import requests

url = "https://akabab.github.io/superhero-api/api/all.json"


def get_data_for_comparison(url):
    response = requests.get(url)
    superheroes_data = response.json()
    return superheroes_data


def heroes_comparison(set_for_comparison, superheroes_data):
    heroes_chart = []
    uncompared_heroes = set_for_comparison.copy()
    compared_heroes = set()

    for hero in superheroes_data:
        if hero['name'] in set_for_comparison:
            entry_in_chart = [hero['powerstats']['intelligence'], hero['name']]
            heroes_chart.append(entry_in_chart)
            uncompared_heroes.remove(hero['name'])
            compared_heroes.add(hero['name'])

    heroes_chart.sort(reverse=True)
    intelligence_champion = heroes_chart[0][1]

    if len(uncompared_heroes) != 0:
         print(f"Мы ничего не знаем о {', '.join(uncompared_heroes)}")
    print(f"Среди {', '.join(compared_heroes)} самый умный - {intelligence_champion}")
    return


if __name__ == '__main__':

    set_for_comparison = {'Hulk', 'Captain America', 'Thanos', 'Noname'}
    heroes_comparison(set_for_comparison, get_data_for_comparison(url))



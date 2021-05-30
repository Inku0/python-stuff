import requests
import json


# steam_key = 'your_key'
# name = the custom url


def get_games(name, steam_key):
    # check the validity

    response_validity = requests.get(f'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?'
                                     f'key={steam_key}&vanityurl={name}')

    # continue if 'No match' is NOT in the response

    if 'No match' not in response_validity.text:

        response_dict = json.loads(response_validity.text)

        steam_id = response_dict['response']['steamid']

        response_games = requests.get(
            f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steam_key}&'
            f'steamid={steam_id}&format=json')

        response_dict = json.loads(response_games.text)

        game_count = response_dict['response']['game_count']

        games = []

        for i in range(game_count):
            games.append(response_dict['response']['games'][i]['appid'])

        return games

    else:
        print('something is wrong!')
        return False


# matches = set(get_games('name1', 'steam_key')) & set(get_games('name2', 'steam_key'))
# print(matches)

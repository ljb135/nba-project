import urllib.request
import gzip
import json


class NBAGame:
    def __init__(self, game_id, json_file):
        self.game_id = game_id
        self.json_file = json_file
        self.home_team_id = None
        self.away_team_id = None
        self.home_team_points = None
        self.away_team_points = None
        self.home_team_players = []
        self.away_team_players = []
        self.home_win = None

        self.__set_team_ids()
        self.__set_points()
        self.__set_player_stats()
        self.__set_result()

    def __set_team_ids(self):
        for i in range(len(self.json_file["resultSets"][2]["rowSet"])):
            if self.json_file["resultSets"][2]["rowSet"][i][0] == self.game_id:
                self.home_team_id = self.json_file["resultSets"][2]["rowSet"][i][1]
                self.away_team_id = self.json_file["resultSets"][2]["rowSet"][i][2]
                return

    def __set_points(self):
        for i in range(len(self.json_file["resultSets"][1]["rowSet"])):
            if self.json_file["resultSets"][1]["rowSet"][i][3] == self.home_team_id:
                self.home_team_points = self.json_file["resultSets"][1]["rowSet"][i][22]
            if self.json_file["resultSets"][1]["rowSet"][i][3] == self.away_team_id:
                self.away_team_points = self.json_file["resultSets"][1]["rowSet"][i][22]
            if self.home_team_points is not None and self.away_team_points is not None:
                return

    def __set_player_stats(self):
        self.json_file = stats_in_game(self.game_id)
        for player in self.json_file["resultSets"][0]["rowSet"]:
            if player[1] == self.home_team_id:
                self.home_team_players.append(player)
            else:
                self.away_team_players.append(player)

    def __set_result(self):
        if self.home_team_points > self.away_team_points:
            self.home_win = True
        else:
            self.home_win = False

    def print(self):
        attrs = vars(self)
        print('\n'.join("%s: %s" % item for item in attrs.items()))


def games_on_date(month, day, year):
    day = f"{month}%2F{day}%2F{year}"
    game_id_url = f"https://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate={day}"
    game_id_headers = {"Host": "stats.nba.com", "Connection": "keep-alive", "Accept": "application/json, text/plain, */*", "x-nba-stats-origin": "stats", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9"}

    req = urllib.request.Request(url=game_id_url, headers=game_id_headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    data = str(gzip.decompress(data), 'utf-8')
    json_file = json.loads(data)
    return json_file


def stats_in_game(game_id):
    game_stats_url = f"https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID={game_id}&RangeType=0&StartPeriod=1&StartRange=0"
    game_stats_headers = {"Host": "stats.nba.com", "Connection": "keep-alive", "Accept": "application/json, text/plain, */*", "x-nba-stats-origin": "stats", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "Referer": f"https://stats.nba.com/game/{game_id}/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9"}

    req = urllib.request.Request(url=game_stats_url, headers=game_stats_headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    data = str(gzip.decompress(data), 'utf-8')
    json_file = json.loads(data)
    return json_file


def get_game_ids(json_file):
    game_list = json_file["resultSets"][0]["rowSet"]
    game_ids = []
    for game in game_list:
        game_ids.append(game[2])
    return game_ids


games = games_on_date("11", "01", "2019")
NBAGame(game_id=get_game_ids(games)[0], json_file=games).print()

# for game_id in get_game_ids(games):
#     stats = stats_in_game(game_id)
#     print(json.dumps(stats, indent=4))

# print(json.dumps(games_on_date("11", "01", "2001"), indent=4))
# print(json.dumps(stats_in_game("0020100019"), indent=4))

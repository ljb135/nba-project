import urllib.request
import gzip
import json


class NBAGame:
    def __init__(self, game_id, json_file):  # object class used to store information regarding a specific NBA Game
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

    # finds the match lineup in "Series Standings" and sets the appropriate values
    def __set_team_ids(self):
        for i in range(len(self.json_file["resultSets"][2]["rowSet"])):  # increment through all games
            if self.json_file["resultSets"][2]["rowSet"][i][0] == self.game_id:  # find matching game
                self.home_team_id = self.json_file["resultSets"][2]["rowSet"][i][1]
                self.away_team_id = self.json_file["resultSets"][2]["rowSet"][i][2]
                return

    # finds the points for each team in "Line Score" and sets the appropriate values
    def __set_points(self):
        for i in range(len(self.json_file["resultSets"][1]["rowSet"])):  # increment through all teams
            if self.json_file["resultSets"][1]["rowSet"][i][3] == self.home_team_id:  # match home id
                self.home_team_points = self.json_file["resultSets"][1]["rowSet"][i][22]
            if self.json_file["resultSets"][1]["rowSet"][i][3] == self.away_team_id:  # match away id
                self.away_team_points = self.json_file["resultSets"][1]["rowSet"][i][22]
            if self.home_team_points is not None and self.away_team_points is not None:  # stops when both are filled
                return

    # finds player stats in "PlayerStats" and sets the appropriate values
    def __set_player_stats(self):
        self.json_file = stats_in_game(self.game_id)  # uses game-specific box score JSON
        for player in self.json_file["resultSets"][0]["rowSet"]:  # increment through all players
            if player[1] == self.home_team_id:  # add player to respective team
                self.home_team_players.append(player)
            else:
                self.away_team_players.append(player)

    # compares scores and determines which team won
    def __set_result(self):
        if self.home_team_points > self.away_team_points:
            self.home_win = True
        else:
            self.home_win = False

    # prints all variables
    def print(self):
        attrs = vars(self)
        print('\n'.join("%s: %s" % item for item in attrs.items()))


# finds all games on a specific day and returns a JSON containing info of all games on that day
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


# finds box score information of a specific game and a JSON containing detailed stats of players in the game
def stats_in_game(game_id):
    game_stats_url = f"https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID={game_id}&RangeType=0&StartPeriod=1&StartRange=0"
    game_stats_headers = {"Host": "stats.nba.com", "Connection": "keep-alive", "Accept": "application/json, text/plain, */*", "x-nba-stats-origin": "stats", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "Referer": f"https://stats.nba.com/game/{game_id}/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9"}

    req = urllib.request.Request(url=game_stats_url, headers=game_stats_headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    data = str(gzip.decompress(data), 'utf-8')
    json_file = json.loads(data)
    return json_file


# returns all the games played on a specific day
def get_game_ids(json_file):
    game_list = json_file["resultSets"][0]["rowSet"]
    game_ids = []
    for game in game_list:
        game_ids.append(game[2])
    return game_ids


games = games_on_date("11", "19", "2019")
game_id_list = get_game_ids(games)
for i in range(len(game_id_list)):
    curr_game_id = game_id_list[i]
    game_info = NBAGame(curr_game_id, games)
    game_data_array = []
    omit_stat_indexes = [10, 13, 16, 20]
    for i in range(len(game_info.home_team_players)):
        for x in range(8, len(game_info.home_team_players[i])):
            if x in omit_stat_indexes:
                continue
            stat = game_info.home_team_players[i][x]
            if stat is None:
                stat = 0
            game_data_array.append(stat)
    for i in range(len(game_info.away_team_players)):
        for x in range(8, len(game_info.away_team_players[i])):
            if x in omit_stat_indexes:
                continue
            stat = game_info.away_team_players[i][x]
            if stat is None:
                stat = 0
            game_data_array.append(stat)

game_data_array.append(int(game_info.home_win))

    print(len(game_data_array))
    print(game_data_array)

# print(game_info.away_team_players[i])

# print(json.dumps(games, indent=4))
# print(json.dumps(game_info.home_team_players, indent=4))
#
# for game_id in get_game_ids(games):
#     stats = stats_in_game(game_id)
#     print(json.dumps(stats, indent=4))

# print(json.dumps(games_on_date("11", "01", "2001"), indent=4))
# print(json.dumps(stats_in_game("0020100019"), indent=4))

import urllib.request
from urllib.error import HTTPError
import gzip
import json
import re
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

db = create_engine('sqlite:///NBAPlayers.db', echo=True)
meta = MetaData()

players = Table('players', meta,
    Column('NAME', String),
    Column('PLAYER_ID', String, primary_key=True),
    Column('YEAR', String),
    Column('AGE', Integer),
    Column('HEIGHT', Integer),
    Column('WEIGHT', Integer),
    Column('MIN', Integer),
    Column('PTS', Integer),
    Column('FGM', Integer),
    Column('FG_PERCENTAGE', Integer),
    Column('THREE_PM', Integer),
    Column('THREE_P_PERCENTAGE', Integer),
    Column('FTM', Integer),
    Column('FT_PERCENTAGE', Integer),
    Column('OREB', Integer),
    Column('DREB', Integer),
    Column('AST', Integer),
    Column('TOV', Integer),
    Column('STL', Integer),
    Column('BLK', Integer),
    Column('PF', Integer),
    Column('PLUS_MINUS', Integer),
    Column('EFG_PERCENTAGE', Integer),
    Column('TS_PERCENTAGE', Integer)
)


# gathers seasonal stats for all players during a specified season
def get_seasonal_stats(season):
    param = f"{season}-{str((season + 1) % 100).zfill(2)}"
    season_stats_url = f"https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={param}&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="
    season_stats_headers = {"Host": "stats.nba.com", "Connection": "keep-alive", "Accept": "application/json, text/plain, */*", "x-nba-stats-origin": "stats", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "Referer": "https://stats.nba.com/players/traditional/?sort=PTS&dir=-1", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9"}

    req = urllib.request.Request(url=season_stats_url, headers=season_stats_headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    data = str(gzip.decompress(data), 'utf-8')
    json_file = json.loads(data)

    season_stats = {}
    for player in json_file["resultSets"][0]["rowSet"]:
        if player[1] is None:
            continue
        player_name = str(player[1])
        del player[31:]
        delete_indexes = [2, 3, 5, 6, 7, 8, 11, 14, 17, 21, 26, 28]
        for index in sorted(delete_indexes, reverse=True):
            del player[index]
        player[0] = str(player[0])
        season_stats[player_name] = [str(season)] + player

    param = f"{season}-{str((season + 1) % 100).zfill(2)}"
    season_stats_url = f"https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Advanced&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={param}&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="
    season_stats_headers = {"Host": "stats.nba.com", "Connection": "keep-alive", "Accept": "application/json, text/plain, */*", "x-nba-stats-origin": "stats", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "Referer": "https://stats.nba.com/players/traditional/?sort=PTS&dir=-1", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9"}

    req = urllib.request.Request(url=season_stats_url, headers=season_stats_headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    data = str(gzip.decompress(data), 'utf-8')
    json_file = json.loads(data)

    for player in json_file["resultSets"][0]["rowSet"]:
        if player[1] is None:
            continue
        player_name = str(player[1])
        del player[29:]
        del player[0: 27]
        try:
            season_stats[player_name] = season_stats[player_name] + player
        except Exception:
            continue

    param = f"{season}-{str((season + 1) % 100).zfill(2)}"
    season_stats_url = f"https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season={param}&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
    season_stats_headers = {"Host": "stats.nba.com", "Connection": "keep-alive", "Accept": "application/json, text/plain, */*", "x-nba-stats-origin": "stats", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "Referer": "https://stats.nba.com/players/traditional/?sort=PTS&dir=-1", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9"}

    req = urllib.request.Request(url=season_stats_url, headers=season_stats_headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    data = str(gzip.decompress(data), 'utf-8')
    json_file = json.loads(data)

    for player in json_file["resultSets"][0]["rowSet"]:
        if player[1] is None:
            continue
        player_name = str(player[1])
        del player[8:]
        del player[0: 6]
        player[1] = int(player[1])
        try:
            season_stats[player_name] = season_stats[player_name] + player
        except Exception:
            continue
    return season_stats


for year in range(1990, 2020):
    print(f"starting {year}")
    player_stats = get_seasonal_stats(year)
    print("finish webscraping")
    for player in player_stats:
        stats = player_stats[player]
        query = players.insert().values(
            NAME=stats[2],
            PLAYER_ID=stats[1],
            YEAR=stats[0],
            AGE=stats[3],
            HEIGHT=stats[22],
            WEIGHT=stats[23],
            MIN=stats[4],
            PTS=stats[18],
            FGM=stats[5],
            FG_PERCENTAGE=stats[6],
            THREE_PM=stats[7],
            THREE_P_PERCENTAGE=stats[8],
            FTM=stats[9],
            FT_PERCENTAGE=stats[10],
            OREB=stats[11],
            DREB=stats[12],
            AST=stats[13],
            TOV=stats[14],
            STL=stats[15],
            BLK=stats[16],
            PF=stats[17],
            PLUS_MINUS=stats[19],
            EFG_PERCENTAGE=stats[20],
            TS_PERCENTAGE=stats[21],
        )
        print("running query")
        conn = db.connect()
        result = conn.execute(query)

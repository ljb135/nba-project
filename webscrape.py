import urllib.request
import gzip


def games_on_date(month, day, year):
    day = f"{month}%2F{day}%2F{year}"
    gameid_url = f"https://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate={day}"
    gameid_headers = {"Host": "stats.nba.com", "Connection": "keep-alive", "Accept": "application/json, text/plain, */*", "x-nba-stats-origin": "stats", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9"}

    req = urllib.request.Request(url=gameid_url, headers=gameid_headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    data = str(gzip.decompress(data), 'utf-8')
    return data


def stats_in_game(game_id):
    gamestats_url = f"https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID={game_id}&RangeType=0&StartPeriod=1&StartRange=0"
    gamestats_headers = {"Host": "stats.nba.com", "Connection": "keep-alive", "Accept": "application/json, text/plain, */*", "x-nba-stats-origin": "stats", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "Referer": "https://stats.nba.com/game/0021900751/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9"}

    req = urllib.request.Request(url=gamestats_url, headers=gamestats_headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    data = str(gzip.decompress(data), 'utf-8')
    return data


print(games_on_date(11, 29, 2003))
print(stats_in_game("0020100265"))


import urllib.request

day = "12%2F07%2F2001"
gameid_url = f"https://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate={day}"
gameid_headers = {"Host": "stats.nba.com", "Accept": "application/json, text/plain, */*", "x-nba-stats-token": "true"}
gameid = "0020100265"
gamestats_url = f"https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID={gameid}&RangeType=0&StartPeriod=1&StartRange=0"

req = urllib.request.Request(url=gameid_url, headers=gameid_headers)
print(gameid_url)
try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)
# the_page = response.read()
# print(the_page)

import urllib.request

url = "https://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate=02%2F05%2F2020"
url = "https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID=0021900757&RangeType=0&Season=2019-20&SeasonType=Regular+Season&StartPeriod=1&StartRange=0"
print(urllib.request.Request(url))

from flask import Flask, url_for, render_template, redirect, jsonify, request, flash
from forms import PlayerForm, PlayerSelectionForm
from numpy import zeros
import os
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select, and_
from predict import run_model


template_dir = os.path.abspath('../../NBA-Project/Web_App/templates')
print(template_dir)

app = Flask(__name__, template_folder=template_dir)
app.config['SECRET_KEY'] = 'ao19s2en1638nsh6msh172kd0s72ksj2'
db = create_engine('sqlite:///NBAPlayers.db', echo=True)
meta = MetaData()

players = Table('players', meta,
    Column('NAME', String),
    Column('PLAYER_ID', String, primary_key=True),
    Column('YEAR', String, primary_key=True),
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


def player_validation(players):
    players_selected = 0
    for player in players:
        if player["year"] != "Empty" and player["player_name"] != "Empty":
            players_selected += 1

    if players_selected < 5:
        return False
    else:
        return True


def get_stats(home_players, away_players):
    num_home_players = 0
    home_stats = []

    for player in home_players:
        year = player["year"]
        player_id = player["player_name"]
        if year != "Empty" and player_id != "Empty":
            print("RUN")
            query = select([players]).where(and_(players.c.YEAR == year, players.c.PLAYER_ID == player_id))
            conn = db.connect()
            result = conn.execute(query)
            result = result.fetchone().values()
            del result[0:3]
            home_stats.extend(result)
            num_home_players += 1

    for x in range(num_home_players, 13):
        home_stats.extend(zeros(21))

    num_away_players = 0
    away_stats = []
    for player in away_players:
        year = player["year"]
        player_id = player["player_name"]
        if year != "Empty" and player_id != "Empty":
            print("RUN")
            query = select([players]).where(and_(players.c.YEAR == year, players.c.PLAYER_ID == player_id))
            conn = db.connect()
            result = conn.execute(query)
            result = result.fetchone().values()
            del result[0:3]
            away_stats.extend(result)
            num_away_players += 1

    for x in range(num_away_players, 13):
        away_stats.extend(zeros(21))

    return home_stats, away_stats


@app.route('/', methods=('GET', 'POST'))
def homepage():
    form = PlayerSelectionForm()

    player_choices = [("Empty", "Empty")]
    for player in form.home_players:
        player.player_name.choices = player_choices
    for player in form.away_players:
        player.player_name.choices = player_choices

    if request.method == "POST":
        home_players = form.home_players.data
        away_players = form.away_players.data

        if not player_validation(away_players) and not player_validation(home_players):
            home_stats, away_stats = get_stats(home_players, away_players)
            prediction = run_model(home_stats, away_stats)
            flash("Please enter 5 players on both teams.", "error")
        elif not player_validation(home_players):
            flash("Please enter 5 players on the home team.", "error")
        elif not player_validation(away_players):
            flash("Please enter 5 players on the away team.", "error")
        else:
            home_stats, away_stats = get_stats(home_players, away_players)
            prediction = run_model(home_stats, away_stats)
            flash("The probability that the home team wins is 50%", "success")

        # home_team_players = {}
        # for i in range(1, 14):
        #     year_label = "home_year_" + str(i)
        #     name_label = "home_" + str(i)
        #     home_team_players[i] = [request.form[year_label], request.form[name_label]]
        # away_team_players = {}
        # for i in range(1, 14):
        #     year_label = "away_year_" + str(i)
        #     name_label = "away_" + str(i)
        #     away_team_players[i] = [request.form[year_label], request.form[name_label]]

    return render_template('request.html', form=form, title='Home')


# @app.route('/prediction', methods=('GET', 'POST'))
# def prediction():
#     return render_template('result.html', title='Prediction')


@app.route('/update/<year>')
def update(year):
    query = select([players.c.PLAYER_ID, players.c.NAME]).where(players.c.YEAR == year)
    conn = db.connect()
    result = conn.execute(query)

    player_array = [{"name": "Empty", "player_id": "Empty"}]

    for player in result:
        playerObj = {}
        playerObj["name"] = player.NAME
        playerObj["player_id"] = player.PLAYER_ID
        player_array.append(playerObj)

    return jsonify({"players": player_array})


if __name__ == '__main__':
    # query = select([players]).where(and_(players.c.YEAR == '2001', players.c.PLAYER_ID == '1502'))
    # conn = db.connect()
    # result = conn.execute(query)
    # result = result.fetchone().values()
    # del result[0:3]
    # print(result)
    app.run(host='0.0.0.0', port=50000, debug=True)

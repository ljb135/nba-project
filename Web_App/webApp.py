from flask import Flask, url_for, render_template, redirect, jsonify
from forms import PlayerForm, PlayerSelectionForm
import os
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select
# from predict import run_model


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


@app.route('/', methods=('GET', 'POST'))
def homepage():
    form = PlayerSelectionForm()
    # query = select([players.c.PLAYER_ID, players.c.NAME]).where(players.c.YEAR == 2007)
    # conn = db.connect()
    # result = conn.execute(query)

    # form.home_players.append_entry(PlayerForm)

    player_choices = [("Empty", "Empty")]
    # for player in result:
    #     player_choices.append((player.PLAYER_ID, player.NAME))
    for player in form.home_players:
        player.player_name.choices = player_choices
    for player in form.away_players:
        player.player_name.choices = player_choices

    if form.validate_on_submit():
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
        return redirect(url_for('prediction'))
    return render_template('request.html', form=form, title='Home')


@app.route('/prediction', methods=('GET', 'POST'))
def prediction():
    return render_template('result.html', title='Prediction')


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

    return jsonify({"players" : player_array})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)

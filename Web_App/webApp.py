from flask import Flask, url_for, render_template, redirect
from forms import PlayerSelectionForm
# from predict import run_model
import os

template_dir = os.path.abspath('../../NBA-Project/Web_App/templates')
print(template_dir)

app = Flask(__name__, template_folder=template_dir)
app.config['SECRET_KEY'] = 'ao19s2en1638nsh6msh172kd0s72ksj2'


@app.route('/', methods=('GET', 'POST'))
def homepage():
    form = PlayerSelectionForm()
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


@app.route('/playerlist', methods=('GET', 'POST'))
def playerlist():
    return render_template('playerlist.html', title='Player List')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)

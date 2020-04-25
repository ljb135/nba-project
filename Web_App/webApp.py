from flask import Flask, url_for, render_template, redirect
from forms import PlayerSelectionForm
import os

template_dir = os.path.abspath('../../NBA-Project/Web_App/templates')
print(template_dir)

app = Flask(__name__, template_folder=template_dir)
app.config['SECRET_KEY'] = 'ao19s2en1638nsh6msh172kd0s72ksj2'


@app.route('/', methods=('GET', 'POST'))
def homepage():  # RENAME
    form = PlayerSelectionForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('request.html', form=form, title='Home')


@app.route('/prediction')
def prediction():
    return render_template('result.html', title='Prediction')


@app.route('/playerlist')
def playerlist():
    return render_template('playerlist.html', title='Player List')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)

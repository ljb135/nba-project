from flask import Flask, url_for, render_template, redirect
from selectionForm import selectionForm

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route('/', methods=('GET', 'POST'))
def contact():
    form = selectionForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

app.run(host='0.0.0.0', port=50000)
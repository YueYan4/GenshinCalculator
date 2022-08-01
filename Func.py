from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    if request.method == 'POST':
        if request.form.get('Resin') == 'Resin':
            return render_template('resin.html')
        if request.form.get('Wish') == 'Wish':
            return render_template('wish.html')
    return render_template('home.html')

@app.route('/resin', methods=['GET', 'POST'])
def resin():
    if request.method == 'POST':
        if request.form.get('Home') == 'Home':
            return render_template('home.html')
    return render_template('resin.html')

@app.route('/wish')
def wish():
    if request.method == 'POST':
        if request.form.get('Home') == 'Home':
            return render_template('home.html')
    return render_template('wish.html')

@app.route('/damage')
def damage():
    if request.method == 'POST':
        if request.form.get('Home') == 'Home':
            return render_template('home.html')
    return render_template('damage.html')
        
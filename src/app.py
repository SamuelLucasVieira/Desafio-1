from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/contatos')
def contato():
    return render_template('contatos.html')

@app.route('/quem_somos')
def quemSomos():
    return render_template('quem somos.html')

app.run()
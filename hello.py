from flask import Flask

app = Flask('__name__')

@app.route('/')# pag. principal
@app.route('/index')
def index():
    return "<h1><center>5toB Informatical</h1></center>"

@app.route('/home/<name>')# Inicio
def home(name):
    return f'<h1>Esto es la pagina de inicio {name}</h1>'

@app.route("/login")
def login():
    return "Bienvenido"

if __name__ == '__main__' :
    app.run(debug=True)

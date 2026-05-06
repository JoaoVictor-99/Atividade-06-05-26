from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Página Inicial'

@app.route('/arearestrita/<id>')
def area(id):

    if id == '1':
        return 'cadeado fechado'

    elif id == '2':
        return 'cadeado aberto'

    else:
        return 'valor inválido'

if __name__ == '__main__':
    app.run(debug=True)
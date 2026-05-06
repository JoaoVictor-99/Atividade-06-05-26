from flask import Flask

app = Flask(__name__)

@app.route('/ola/<nome>')
def ola(nome):
    return f"Ola, {nome} Seja bem-vindo."

if __name__ == '__main__':
    app.run(debug=True)
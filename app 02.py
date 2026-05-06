from flask import Flask

app = Flask(__name__)

@app.route('/calculo/<int:n1>/<int:n2>')
def soma(n1, n2):
    soma = n1 + n2
    return f"{n1} + {n2} = {soma}"

if __name__ == '__main__':
    app.run(debug=True)
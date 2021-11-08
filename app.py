from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'hi': 'yeah'}
    

@app.route('/dog/<string:raca>')
def dog(raca: str):
    return f'<h1> a raca do dog eh {raca} <h1>'


if __name__ == '__main__':
    app.run(debug=True)
    
from flask import Flask, render_template

app = Flask(__name__, static_folder='./templates')

@app.route('/')
def hello_world():
    return {'hi': 'yeah'}
    

@app.route('/dog/<string:raca>')
def dog(raca: str):
    return f'<h1> a raca do dog eh {raca} <h1>'



@app.route('/person/<string:name>')
def get_person(name: str):
    return render_template('hello.html', name= name)



if __name__ == '__main__':
    app.run(debug=True)

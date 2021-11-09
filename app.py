from flask import Flask, render_template
from flask_restx import Api, Resource
from flask_admin import Admin

app = Flask(__name__, static_folder='./templates')
app.config['FLASK_ADMIN_SWATCH'] = 'darkly'
admin = Admin(app, name='admin area', template_mode='bootstrap3')
api = Api(app, title="minha api", description="description for api")

@app.route('/', methods=['GET'])
def hello_world():
    return {'hi': 'yeah'}

@app.route('/dog/<string:raca>', methods=['GET'])
def dog(raca: str):
    return f'<h1> a raca do dog eh {raca} <h1>'


@app.route('/person/<string:name>', methods=['GET'])
def get_person(name: str):
    return render_template('hello.html', name= name)



# !!!!!!!!!!!!!!!!API !!!!!!!!!!!!!!!

@api.route('/doc/')
class HelloApi(Resource):
    def get(self):
        return {'hi': 'yeah'},200
    def post(self):
        return {'hi': 'yeah'},201
    def put(self):
        return {'hi': 'yeah'},404
    def delete(self):
        return {'hi': 'yeah'},403
    def patch(self):
        return {'hi': 'yeah'},500






if __name__ == '__main__':
    app.run(debug=True)

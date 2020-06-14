from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {'Applicatin': 'BackPoint'}


@app.route('/contacts')
def posts():
    return {
        'FirstName': 'Harrison',
        'LastName': 'Ford',
        'Born': '07/13/1942',
        'BirthCity': 'Chicago',
        'Roles': [
            'Hans Solo',
            'Indiana Jones',
            'Rick Deckard '
        ]}


@app.route('/user/<username>')
def userdata(username):
    return {'Username': username, 'Description': 'This data comes from the backend app'}


if __name__ == '__main__':
    app.run()

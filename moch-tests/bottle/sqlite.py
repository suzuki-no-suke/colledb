from bottle import route, run, template
import os

# setup bottle - sqlite
app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='./data/test.db')
app.install(plugin)

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/add/:id')
def add_id(id, db):
    # insert id into db
    db.execute('INSERT INTO test (specified_id) VALUES (?)', id).fetchone()
    return template('{{id}} is added')

@route('/show/:item')
def show_id(item, db):
    row = db.execute('SELECT * FROM test WHERE specified_id=?', item).fetchone()
    if row:
        return template('showitem', page=row)
    return template('not found : {{item}}')

SERVER_ADDRESS = '192.168.0.1'
SERVER_PORTNO = 80
if "SERVER_ADDRESS" in os.environ:
    SERVER_ADDRESS = os.environ["SERVER_ADDRESS"]

print("Server -> {}:{}".format(SERVER_ADDRESS, SERVER_PORTNO))

run(host=SERVER_ADDRESS, port=SERVER_PORTNO)


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
    



SERVER_ADDRESS = '192.168.0.1'
SERVER_PORTNO = 80
if "SERVER_ADDRESS" in os.environ:
    SERVER_ADDRESS = os.environ["SERVER_ADDRESS"]

print("Server -> {}:{}".format(SERVER_ADDRESS, SERVER_PORTNO))

run(host=SERVER_ADDRESS, port=SERVER_PORTNO)


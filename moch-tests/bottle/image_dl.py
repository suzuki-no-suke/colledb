from bottle import route, run, template, static_file
import bottle.ext.sqlite
import bottle
import os

# setup bottle - sqlite
app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='./test.db')
app.install(plugin)


# directory roots
ROOT_DIR = '/var/www/html'
if "ROOT_DIR" in os.environ:
    ROOT_DIR = os.environ["ROOT_DIR"]
SAMPLE_ROOT = ROOT_DIR + '/sampledata'


# routing
@app.route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@app.route('/add/:id')
def add_id(id, db):
    # insert id into db
    db.execute('INSERT INTO test (specified_id) VALUES (?)', (id,))
    db.commit()
    return template('{{id}} is added')

@app.route('/show/:item')
def show_id(item, db):
    print("id -> {}".format(item))
    row = db.execute('SELECT * FROM test WHERE specified_id=?', (item,)).fetchone()
    if row:
        print(row)
        return template('<p>data display : {{row}}</p>', row=row)
    return template('not found : {{item}}')

@app.route('/sampledata/<filename:path>')
def sample(filename):
    print("root => {}".format(os.path.join(os.path.abspath(SAMPLE_ROOT))))
    return static_file(filename, root=SAMPLE_ROOT)

@app.route('/dltest/lenna')
def directory_download_renna():
    print("rot => {}".format(os.path.abspath(SAMPLE_ROOT)))
    return static_file('./l_hires.jpg', root=SAMPLE_ROOT)


# server setting
SERVER_ADDRESS = '192.168.0.1'
SERVER_PORTNO = 80
if "SERVER_ADDRESS" in os.environ:
    SERVER_ADDRESS = os.environ["SERVER_ADDRESS"]

print("Server -> {}:{}".format(SERVER_ADDRESS, SERVER_PORTNO))

app.run(host=SERVER_ADDRESS, port=SERVER_PORTNO)


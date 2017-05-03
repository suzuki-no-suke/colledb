from bottle import route, run, template, request
import bottle.ext.sqlite
import bottle
import os
import simplejson as json
import uuid
import datetime

# setup bottle - sqlite
app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='./test.db')
app.install(plugin)

# app config
## server address
SERVER_ADDRESS = 'localhost'
SERVER_PORTNO = 80
if "SERVER_ADDRESS" in os.environ:
    SERVER_ADDRESS = os.environ["SERVER_ADDRESS"]
print("Server -> {}:{}".format(SERVER_ADDRESS, SERVER_PORTNO))

## image directory
ROOT_PATH="."
if "ROOT_PATH" in os.environ:
    ROOT_PATH = os.environ["ROOT_PATH"]
DATA_DIR=ROOT_PATH + "/data"


# routing
@app.get('/list')
def list_all(db):
    all_books = db.execute('SELECT * FROM books').fetchall()
    response_dict = {'books': []}
    if all_books:
        for book in all_books:
            summary = 
            book_data = {
                'ID': book['id'],
                'title': book[''],
                'summary': summary
            }
            response_dict['books'].append(book_data)
    bottle.response.headers['Content-Type'] = 'application/json'
    return json.dumps(response_dict)

@app.post('/book')
def add_book(db):
    # gether book information
    title = request.forms.get['title']
    author = request.forms.get['author']
    tags = request.forms.get['tags']
    now = datetime.now
    created = now.tostring('YYYY-MM-DD HH:MM:SS')  # NOTE : localtime
    updated = now.tostring('YYYY-MM-DD HH:MM:SS')

    # process book image
    image_keys = ['image1', 'image2', 'image3', 'image4']
    image_id_dict = {}
    for key in image_keys:
        if key in request.files:
            upfile = request.files.get(key)
            file_id = uuid.uuid4()
            extension = os.path.splitext(upfile.filename)(1)
            filename = file_id + extension
            filepath = DATA_DIR + '/' + filename
            with open(filepath, "wb") as fimg:
                fimg.write(upfile.read())
            image_id_dict[key] = filename

    # insert into database
    if title and author and tags:
        insert_query = """
        INSERT INTO books (
            id,
            title,
            author,
            tags,
            created,
            updated,
            {}
        ) VALUES (
            ?, 
            ?,
            ?,
            ?,
            ?,
            ?,
            {}
        )
        """[1:-1].format(
            ','.join(image_id_dict.keys()),
            ','.join([',' in image_id_dict])
        )
        db.execute(insert_query)
        db.commit()

    # build response
    idrow = db.execute('SELECT last_insert_rowid()')
    id = idrow[0]
    response_dict = {'ID': id}
    bottle.response.headers['Content-Type'] = 'application/json'
    return json.dumps(response_dict)


# under construction
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

# admin commands
@app.route('/admin/alive')
def admin_alive():
    return "alive"


# run server
app.run(host=SERVER_ADDRESS, port=SERVER_PORTNO, reloader=True)


from bottle import route, get, post, abort, run, template, static_file, request
import bottle.ext.sqlite
import bottle
import os
import uuid
import datetime


# app config
## server address
SERVER_ADDRESS = '192.168.1.0'
SERVER_PORTNO = 80
if "SERVER_ADDRESS" in os.environ:
    SERVER_ADDRESS = os.environ["SERVER_ADDRESS"]
print("Server -> {}:{}".format(SERVER_ADDRESS, SERVER_PORTNO))


## api server address
API_SERVER_ADDRESS = 'localhost'
if "API_SERVER_ADDRESS" in os.environ:
    API_SERVER_ADDRESS = os.environ["API_SERVER_ADDRESS"]
print("API server -> {}:80".format(API_SERVER_ADDRESS))


## root path
ROOT_PATH = "."
if "ROOT_PATH" in os.environ:
    ROOT_PATH = os.environ["ROOT_PATH"]
print("root path -> {}".format(ROOT_PATH))

DATA_PATH = os.path.abspath(ROOT_PATH + "/data")
DB_PATH = os.path.abspath(ROOT_PATH + "/data/data.db")


# install sqlite3 plugin
app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(DB_PATH)
app.install(plugin)

# set template path
bottle.TEMPLATE_PATH.insert(0, os.path.abspath(ROOT_PATH + "/view/"))


# routing
@app.route('/')
@app.route('/app/list')
def show_list():

    # temporary link to pages
    tmp = """
    <a href="/app/add">add form</a>
    """[1:-1]
    return tmp
    #return template('page_list', book_list=books)



@app.get('/app/book/<id>')
def show_book(id, db):
    # gether book information
    row = db.execute('SELECT * FROM books WHERE id = ?', id).fetchone()
    if row:
        book = {}
        book['id'] = row['id']
        book['title'] = row['title']
        book['author'] = row['author']
        book['tags'] = row['tags']

        # gether image information
        img_nos = []
        for no in range(1, 4):
            img_key = "image{}".format(no)
            if row[img_key] and row[img_key] != string.empty:
                img_nos.insert(0, no)

        return template('page_show_book', book=book, image_nos=img_nos)
    return abort(404, "book id {} is not found.".format(id))

@app.post('/app/book/<id>')
def update_book_and_show(id):
    return 'NOT IMPLEMENT <a href="/"> top page </a>'

@app.get('/app/edit/<id>')
def edit_book_form(id):
    return 'NOT IMPLEMENT <a href="/"> top page </a>'


@app.get('/app/add')
def add_newbook_form():
    return template('page_add_book')


@app.post('/app/add')
def add_newbook_and_show_next_form(db):
    # utf-8 workaround
    db.text_factory = str

    # for debug 
    print("forms")
    for k, v in request.forms.items():
        print("{} -> {}".format(k,v))
    print("files")
    for k, v in request.files.items():
        print("{} -> {}".format(k,v))

    # gether post information
    b_title = request.forms.get('title')
    b_author = request.forms.get('author') 
    b_tags = request.forms.get('tags')

    # save files
    image_keys = ['image1', 'image2', 'image3', 'image4']
    file_ids = {}
    for imkey in image_keys:
        if imkey in request.files:
            print("key {} - found".format(imkey))
            img = request.files.get(imkey)
            print("filename -> {}".format(img.filename))
            img_name = img.filename
            if img_name and not img_name.isspace():
                print("filename -> {}".format(img_name))
                ext = os.path.splitext(img_name)
                im_uuid = uuid.uuid4()
                im_filename = str(im_uuid) + ext[1]
                print("save file name -> {}".format(im_filename))
                im_path = os.path.abspath(DATA_PATH + "/" + im_filename)
                with open(im_path, "wb") as fimg:
                    fimg.write(img.file.read())
                file_ids[imkey] = im_filename

    # query keys
    img_query_keys = [key for key in image_keys if key in file_ids.keys()]
    img_file_names = tuple(file_ids[key] for key in img_query_keys)

    # build datetime
    now = datetime.datetime.now()
    b_created = now.strftime('%Y-%m-%d %H:%M:%S')
    b_updated = now.strftime('%Y-%m-%d %H:%M:%S')

    # build and execute query
    all_keys = ['title', 'author', 'tags', 'created', 'updated'] + img_query_keys 
    query_marks = ['?' for k in all_keys]
    query_param_tuple = (b_title, b_author, b_tags, b_created, b_created,) \
        + img_file_names
    query = """
    INSERT INTO books (
        {}
    ) VALUES (
        {}
    )
    """[1:-1]
    filled_query = query.format(
        ','.join(all_keys),
        ','.join(query_marks))
    print("filled query -> " + filled_query)
    db.execute(filled_query, query_param_tuple)
    db.commit()

    # show new form
    return template('page_add_book')


@app.get('/image/<book_id>/<image_no:int>')
def get_book_image(book_id, image_no, db):
    print("request -> book {} / image {}".format(book_id, image_no))
    # check image_no
    if not (image_no >= 1 and image_no <= 4):
        return abort(404, 'image - wrong image_not') 
    # get image uuid
    img_key = "image{}".format(image_no) 
    query = 'SELECT {} AS img_id FROM books WHERE id = ?'.format(img_key)
    print("image query -> {}".format(query))
    row = db.execute(query, book_id).fetchone()
    if row:
        img_id = row['img_id']
        file_path = os.path.abspath(DATA_PATH + "/" + img_id)
        print("file -> {}".format(file_path))
        if os.path.exists(file_path):
            # TODO : not safe
            return static_file(img_id, root=DATA_PATH)
    abort(404, "file not found")

@app.error(404)
def on_404(error):
    return '404, <a href="/">goto toppage</a>' + error.body


app.run(host=SERVER_ADDRESS, port=SERVER_PORTNO)


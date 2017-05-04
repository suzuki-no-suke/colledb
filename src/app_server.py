from bottle import route, run, template
import bottle
import simplejson as json


# app config
## server address
SERVER_ADDRESS = '192.168.1.0'
SERVER_PORTNO = 80
if "SERVER_ADDRESS" in os.environ:
    SERVER_ADDRESS = os.environ["SERVER_ADDRESS"]
print("Server -> {}:{}".format(SERVER_ADDRESS, SERVER_PORTNO))


## api server address
API_SERVER_ADDRESSS = 'localhost'
if "API_SERVER_ADDRESS" in os.environ:
    API_SERVER_ADDRESS = os.environ["API_SERVER_ADDRESS"]
print("API server -> {}:80".format(API_SERVER_ADDRESS))


# routing
@route('/')
@route('/app/list')
def show_list():

    books = [
        {"id": 1, "image1": 1, "title": "test", "author": "test", "tags": ""},
        {"id": 2, "image1": 2, "title": "test2", "author": "test2", "tags": "tags"},
    ]
    return template('page_list', book_list=books)

@get('/app/book/<id>')
def show_book(id):

    return "NOT IMPLEMENT"

@post('/app/book/<id>')
def update_book_and_show(id):
    return "NOT IMPLEMENT"

@get('/app/edit/<id>')
def edit_book_form(id):
    return "NOT IMPLEMENT"


@get('/app/add')
def add_newbook_form():
    return template('page_add_book')


@post('/app/add')
def add_newbook_and_show_next_form():
    # process add data

    # show new form
    return template('page_add_book')



# run server
app.run(host=SERVER_ADDRESS, port=SERVER_PORTNO, reloader=True)


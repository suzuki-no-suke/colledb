from bottle import route, get, post, run, template
import bottle
import os


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

bottle.TEMPLATE_PATH.insert(0, os.path.abspath(ROOT_PATH + "/view/"))
DATA_PATH = os.path.abspath(ROOT_PATH + "/data")



# routing
@route('/')
@route('/app/list')
def show_list():

    # temporary link to pages
    tmp = """
    <a href="/app/add">add form</a>
    """[1:-1]
    return tmp
    #return template('page_list', book_list=books)



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
run(host=SERVER_ADDRESS, port=SERVER_PORTNO, reloader=True)


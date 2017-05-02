from bottle import route, run, template
import bottle
import os

# routing
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/template/<id>')
def template_id(id):
    return template('test_template', id=id)


# server setting
SERVER_ADDRESS = '192.168.0.1'
SERVER_PORTNO = 80
if "SERVER_ADDRESS" in os.environ:
    SERVER_ADDRESS = os.environ["SERVER_ADDRESS"]

print("Server -> {}:{}".format(SERVER_ADDRESS, SERVER_PORTNO))

run(host=SERVER_ADDRESS, port=SERVER_PORTNO)


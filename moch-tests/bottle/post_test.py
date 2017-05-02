from bottle import route, run, template, request
import bottle
import os

# routing
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/form')
def show_form():
    return template('')

@route('/post', method='POST')
def proc_post():
    title = request.forms.get('title')
    file = request.files.get('uploaded')
    print("title = {} / file = {}".format(title, file))
    if title and file:
        raw = data.file.read()  # read all of file
        filename = data.filename
        filelen = len(raw)
        mesg = "Upload succeed, file - {} ({} bytes.)".format(filename, filelen)
        print(mesg)
        return template("Upload succeed, file - {{fname}} ({{size}} bytes.)", filename, filelen)
    return template('post failed.')

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


import requests
import bottle
import os

# server setting
SERVER_ADDRESS = '192.168.0.1'
SERVER_PORTNO = 80
if "SERVER_ADDRESS" in os.environ:
    SERVER_ADDRESS = os.environ["SERVER_ADDRESS"]

print("Server -> {}:{}".format(SERVER_ADDRESS, SERVER_PORTNO))

# API Server
@bottle.route('/api/hello/<name>')
def index(name):
    return bottle.template('<b>Hello {{name}}</b>!', name=name)

@bottle.route('/api/submit', method='POST')
def submit():
    title = request.forms.get('title')
    upload = request.files.get('upload')
    print("api - title = {} / file = {}".format(title, upload))

    if title and upload:
        # save file
        upload.save("./image.jpg", overwrite=True)
        return "Data saved"
    return "Upload failed"

@bottle.route('/api/look')
def look():
    return bottle.static_file("./image.jpg")


# App Server
@bottle.route('/app/form')
def form():
    return template('test_form')


@bottle.route('/post', method="POST")
def app_post():
    # redirect ? to /api/submit
    return "not implemented"

@bottle.route('/app/see')
def app_see():
    geturl = "http://{}/api/look".format(SERVER_ADDRESS)
    r = requests.get(geturl)
    return r.content

bottle.run(host=SERVER_ADDRESS, port=SERVER_PORTNO)


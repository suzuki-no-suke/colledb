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
    title = bottle.request.forms.get('title')
    upload = bottle.request.files.get('uploaded')
    print("api - title = {} / file = {}".format(title, upload))

    for k, v in bottle.request.POST.items():
        print("{} -> {}".format(k ,v))

    if title and upload:
        # save file
        upload.save("./image.jpg", overwrite=True)
        return "Data saved"
    return "Upload failed"

@bottle.route('/api/look')
def look():
    return bottle.static_file("./image.jpg", root=".")


# App Server
@bottle.route('/app/form')
def form():
    return bottle.template('test_form')


@bottle.route('/post', method="POST")
def app_post():
    # redirect ? to /api/submit
    title = bottle.request.forms.get('title')
    uploaded = bottle.request.files.get('uploaded') 
    print("title {} / data {}".format(title, uploaded))

    if title and uploaded:
        # multpart file parameters
        files = {'uploaded' : uploaded.file}
        postdata = {'title': title}
        r = requests.post("http://localhost/api/submit", data=postdata, files=files)
        return r.text 
    return "wrong post parameters"

@bottle.route('/app/see')
def app_see():
    geturl = "http://{}/api/look".format('localhost')
    r = requests.get(geturl)
    resp = bottle.HTTPResponse(status=200, body=r.content)
    resp.content_type = 'image/jpg'
    resp.set_header('Content-Length', str(len(r.content)))
    return resp 

bottle.run(host=SERVER_ADDRESS, port=SERVER_PORTNO)


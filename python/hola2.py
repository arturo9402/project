from bottle import route, run, template

@route('/')
def index():
    return template('<b>hola mundo</b>!')

run(host='localhost', port=8080)
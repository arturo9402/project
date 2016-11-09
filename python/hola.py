from bottle import route, run, template

@route('/hola/<name>')
def index(name):
    return template('<b>hola {{name}}</b>!', name=name)

run(host='localhost', port=8080
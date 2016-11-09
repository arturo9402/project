from bottle import route, run, template

@route('/suma/<x>/<y>')
def index(x,y):
    return template('<b>suma {{x}}, {{y}}</b>!', x=x, y=y)

run(host='localhost', port=8080)
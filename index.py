from bottle import route, run, static_file, request, response
import json
from calculator import calc


@route('/')
def sumar():
    return static_file('index.html', root='./')


@route('/sumar', method="POST")
def sumar():
    response.content_type = 'application/json'
    return json.dumps({
        "result": calc(request.json['first_number'], request.json['second_number'])
    })


run(host='localhost', port=5000)

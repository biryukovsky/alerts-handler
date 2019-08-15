from flask import request, Response
from app import app


@app.route('/')
def index():
    return 'Hello'


@app.route('/alerts', methods=['POST', 'PUT',])
def alerts():
    data = request.json
    print(data)
    return Response(status=200)

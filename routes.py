import json
from datetime import datetime

from flask import request, Response
from app import app
from utils import influx_client, render_query


@app.route('/')
def index():
    return 'Hello'


@app.route('/alerts', methods=['POST', 'PUT',])
def alerts():
    data = request.json
    data['date'] = datetime.today()
    data['ruleUrl'] = data['ruleUrl'].replace('localhost', app.config['HOST'])

    tags = {
        'ruleName': data['ruleName'],
        'state': data['state'],
    }

    if not data['evalMatches']:
        influx_client.write_points([
            render_query(
                measurement=app.config['INFLUX_MEASUREMENT'],
                tags=tags,
                time=data['date']
            )
        ])
        return Response(status=200)

    query = []

    for match in data['evalMatches']:
        query.append(
            render_query(
                measurement=app.config['INFLUX_MEASUREMENT'],
                tags=tags,
                time=data['date'],
                value=float(match['value'])
            )
        )

    influx_client.write_points(query)

    return Response(status=200)

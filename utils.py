import re

from influxdb import InfluxDBClient
from app import app


influx_client = InfluxDBClient(
    host=app.config['INFLUX_HOST'],
    port=app.config['INFLUX_PORT'],
    database=app.config['INFLUX_DB_NAME'],
    ssl=app.config['INFLUX_HTTPS'])


def render_query(measurement, tags, time, value):
    output = {
        'measurement': measurement,
        'tags': tags,
        'time': time,
        'fields': {
            'value': value
        }
    }

    return output


def parse_rule_name(rule_name):
    branch = re.search(r'([Оо]тдел.+?\s)([0-9]+)', rule_name)
    if not branch or not branch.groups():
        raise ValueError
    return branch.groups()[1]

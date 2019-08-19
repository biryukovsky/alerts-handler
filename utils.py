import re

from influxdb import InfluxDBClient
from app import app


influx_client = InfluxDBClient(
    host=app.config['INFLUX_HOST'],
    port=app.config['INFLUX_PORT'],
    database=app.config['INFLUX_DB_NAME'],
    ssl=app.config['INFLUX_HTTPS'])


def render_query(measurement, tags, time, value=None):
    output = {
        'measurement': measurement,
        'tags': tags,
        'time': time,
        'fields': {
            'value': value
        }
    }
    if value is None:
        output.pop('fields')

    return output

def parse_rule_name(rule_name):
    return

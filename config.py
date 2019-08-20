import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    HOST = os.getenv('HOST')

    BASE_AUTH_USER = os.getenv('BASE_AUTH_USER')
    BASE_AUTH_PASSWORD = os.getenv('BASE_AUTH_PASSWORD')

    INFLUX_HOST = os.getenv('INFLUX_HOST')
    INFLUX_PORT = os.getenv('INFLUX_PORT')
    INFLUX_DB_NAME = os.getenv('INFLUX_DB_NAME')
    INFLUX_HTTPS = bool(int(os.getenv('INFLUX_HTTPS')))
    INFLUX_MEASUREMENT = os.getenv('INFLUX_MEASUREMENT') or 'alerts'

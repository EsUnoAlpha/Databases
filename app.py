from flask import Flask
import psycopg2
from psycopg2.extras import RealDictCursor


def get_pg_connection():
    connection = psycopg2.connect("""
    password=postgres dbname=postgres user=postgres port=38746 host=localhost
    """, cursor_factory=RealDictCursor)
    connection.autocommit = True
    return connection

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello_world():
    return "<p>Jesus, that is working!!!</p>"

@app.route("/holders")
def get_holders():
    with get_pg_connection() as connection, connection.cursor() as cur:
        cur.execute('select * from holder')
        holders = cur.fetchall()

    return holders

@app.route("/holders/create")
def create_holders():
    name = 'alex'
    phone = '0005'

    with get_pg_connection() as connection, connection.cursor() as cur:
        cur.execute(f"insert into holder(name, phone) values('{name}', '{phone}')")

    return {'msg':'created.'}



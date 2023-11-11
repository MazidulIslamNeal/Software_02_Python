from flask import Flask, request, Response
import json
import mysql.connector


connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
)

app = Flask(__name__)

@app.route('/airport/<string:icao>')
def airport(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            name = row[0]
            location = row[1]

    response = {
        "Airport" : name,
        "Location" : location,
        "ICAO" : icao
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

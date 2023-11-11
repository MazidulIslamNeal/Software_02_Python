from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/prime_number/<number>')
def prime_number(number):
    isPrime = True
    number = int(number)
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                isPrime = False
                break

    response = {
        "isPrime": isPrime,
        "Number": number
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

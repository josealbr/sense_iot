from flask import Flask, render_template, redirect, jsonify
from sense_hat import SenseHat

app = Flask(__name__)

sense = SenseHat()

@app.route("/")
def main_page():
    sense.show_letter('H')
    return 'HELLO RASPBERRY'


@app.route("/temperature")
def temp():
    temp = sense.get_temperature() - 6
    return jsonify(temperature=temp)


@app.route("/humidity")
def humidity():
    humidity = sense.get_humidity()
    return jsonify(humidity=humidity)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
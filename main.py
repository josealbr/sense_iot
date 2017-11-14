from flask import Flask, render_template, redirect, jsonify
from sense_hat import SenseHat
import time

app = Flask(__name__)

sense = SenseHat()
red = (255, 0, 0)

@app.route("/")
def main_page():
    sense.show_letter('H')
    sense.clear(red)
    time.sleep(0.3)
    sense.clear((0, 0, 0))
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
from flask import Flask, render_template, redirect, jsonify
from sense_hat import SenseHat


app = Flask(__name__)

sense = SenseHat()
red = (255, 0, 0)


@app.route("/")
def main_page():
    sense.show_message("Hola")
    return 'HELLO RASPBERRY'


@app.route("/temperature")
def temp():
    t = sense.get_temperature() - 6
    return jsonify(temperature=temp)


@app.route("/humidity")
def humidity():
    h = sense.get_humidity()
    return jsonify(humidity=h)


@app.route("/pressure")
def pressure():
    p = sense.get_pressure()
    return jsonify(pressure=p)


@app.route("/others")
def situation():
    a = sense.get_accelerometer()
    g = sense.get_gyroscope()
    c = sense.get_compass()
    o = sense.get_orientation_degrees()
    return jsonify(acceleration=a,
                   gyro=g,
                   compass=c,
                   orientation=o)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
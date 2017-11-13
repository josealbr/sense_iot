from flask import Flask, render_template, redirect, jsonify
from sense_hat import SenseHat

app = Flask(__name__)

sense = SenseHat()

@app.route("/")
def main_page():
    sense.show_letter('H')
    return 'HELLO RASPBERRY'

@app.route("/temp")
def temp():
    temp = sense.get_temperature() - 6
    return jsonify(temp)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
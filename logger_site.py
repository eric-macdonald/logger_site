from flask import Flask, render_template
import subprocess
import os
from datetime import datetime
from envirophat import weather
from envirophat import light
from envirophat import analog
from envirophat import leds

LEDout = False

app = Flask(__name__)

@app.route("/")
def check():
    with open("log.txt", "r") as f:
        content = f.read()
    return render_template("template.html", content=content)

if __name__ == "__main__":
       app.run(host='0.0.0.0', port=5000, debug=True)


from flask import Flask, render_template, redirect, url_for
import random
from datetime import datetime

app = Flask(__name__)

pump_status = "OFF"

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/dashboard")
def dashboard():
    global pump_status
    moisture = random.randint(20, 80)
    last_irrigation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template(
        "dashboard.html",
        moisture=moisture,
        pump_status=pump_status,
        last_irrigation=last_irrigation
    )

@app.route("/pump/start")
def start_pump():
    global pump_status
    pump_status = "ON"
    return redirect(url_for('dashboard'))

@app.route("/pump/stop")
def stop_pump():
    global pump_status
    pump_status = "OFF"
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)

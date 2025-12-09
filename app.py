from flask import Flask, render_template, request

app = Flask(__name__)

history = []  # store moisture readings


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        try:
            moisture = int(request.form["moisture"])
            moisture_limit = 40  # threshold

            if moisture < moisture_limit:
                result = "Irrigation Needed 💧 — Soil moisture is too low."
            else:
                result = "No Irrigation Needed 🌤️ — Soil moisture is okay."

            # save to history
            history.append({"moisture": moisture, "result": result})

        except ValueError:
            result = "Invalid Input! Please enter a number."

    return render_template("index.html", result=result)


@app.route("/history")
def view_history():
    return render_template("history.html", history=history)


if __name__ == "__main__":
    app.run(debug=True)

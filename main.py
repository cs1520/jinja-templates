from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/now")
@app.route("/time")
def show_time():
    now = datetime.datetime.now()
    return render_template("time.html", time=now)


f = ["Apples", "Oranges", "Bananas", "Pears", "Cherries"]
v = ["Spinach", "Broccoli", "Carrots"]
foods = { "fruits": f, "vegetables": v }

@app.route("/foods")
def show_list():
        return render_template("foods.html", foods=foods)

@app.route("/foods.json")
def show_foods_json():
    return jsonify(foods)


if __name__ == "__main__":
    app.run()

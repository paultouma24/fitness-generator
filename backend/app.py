from fitness_generator import LIFT_HISTORY_STRS
from fitness_generator import save_workout
from fitness_generator import LiftWorkout


from flask import Flask, render_template

app = Flask(__name__)

latest_workout = None
app.template_folder = "../frontend/templates"


@app.template_filter("newline_to_br")
def newline_to_br(value):
    return value.replace("\n", "<br>")


@app.route("/")
def index():
    return render_template("main.html", history=LIFT_HISTORY_STRS[::-1])


@app.route("/generate", methods=["POST"])
def generate():
    global latest_workout
    latest_workout = LiftWorkout()
    return render_template(
        "main.html",
        workout=str(latest_workout),
        history=LIFT_HISTORY_STRS[::-1],
    )


@app.route("/approve", methods=["POST"])
def approve():
    global latest_workout
    save_workout(latest_workout)
    latest_workout = None
    return render_template("main.html", history=LIFT_HISTORY_STRS[::-1])


if __name__ == "__main__":
    app.run()

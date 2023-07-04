from fitness_generator import WorkoutGeneratorUtility
from flask import Flask, render_template

app = Flask(__name__)

app.template_folder = "../frontend/templates"


def main_template():
    latest_workout = WorkoutGeneratorUtility.latest_workout
    return render_template(
        "main.html",
        workout="" if not latest_workout else latest_workout,
        history=WorkoutGeneratorUtility.get_workout_history(),
    )


@app.route("/")
def index():
    WorkoutGeneratorUtility.load_workouts()
    return main_template()


@app.route("/generate", methods=["GET"])
def generate():
    WorkoutGeneratorUtility.generate_workout()
    return main_template()


@app.route("/approve", methods=["POST"])
def approve():
    WorkoutGeneratorUtility.save_workout()
    return main_template()


if __name__ == "__main__":
    app.run()

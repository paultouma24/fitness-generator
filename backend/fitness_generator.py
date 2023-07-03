import random

from config import LIFTING_EXERCISES, LiftCategory

LIFT_HISTORY_STRS = []
LIFT_HISTORY = []


class LiftWorkout:
    def __init__(self):
        self.exercises = {
            LiftCategory.CHEST: None,
            LiftCategory.BACK: None,
            LiftCategory.HINGE: None,
            LiftCategory.SHRUG: None,
            LiftCategory.SHOULDER: None,
            LiftCategory.PRESS: None,
            LiftCategory.BICEPS: None,
            LiftCategory.TRICEPS: None,
            LiftCategory.CORE: None,
            LiftCategory.CALVES: None,
        }

        self.populate_workout()

    def populate_workout(self):
        exercise_categories = {
            LiftCategory.CHEST: [],
            LiftCategory.BACK: [],
            LiftCategory.HINGE: [],
            LiftCategory.SHRUG: [],
            LiftCategory.SHOULDER: [],
            LiftCategory.PRESS: [],
            LiftCategory.BICEPS: [],
            LiftCategory.TRICEPS: [],
            LiftCategory.CORE: [],
            LiftCategory.CALVES: [],
        }

        for exercise in LIFTING_EXERCISES:
            exercise_categories[exercise.category].append(exercise)

        # Get the last two workouts from LIFT_HISTORY
        look_back_window = []
        if LIFT_HISTORY:
            if len(LIFT_HISTORY) == 1:
                look_back_window = [LIFT_HISTORY[0]]
            else:
                look_back_window = LIFT_HISTORY[-2:]

        # Exclude exercises from the last two workouts
        excluded_exercises = set()
        for workout in look_back_window:
            for exercise in workout.exercises.values():
                if exercise:
                    excluded_exercises.add(exercise)
        # Select exercises for the current workout, excluding the excluded exercises
        for category in exercise_categories:
            available_exercises = [
                exercise
                for exercise in exercise_categories[category]
                if exercise not in excluded_exercises
            ]
            exercise = random.choice(available_exercises)
            self.exercises[category] = exercise

    def __str__(self):
        workout_str = ""
        for category, exercise in self.exercises.items():
            workout_str += f"{category.name}: {exercise.name}<br>"
        return workout_str


def save_workout(workout: LiftWorkout):
    # save to DB eventually
    LIFT_HISTORY_STRS.append(str(workout))
    LIFT_HISTORY.append(workout)

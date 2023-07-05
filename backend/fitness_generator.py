import pickle
import random
from typing import List, Optional

from workout_config import LIFTS_BY_BODY_PART, BodyPart, Exercise, LiftWorkout

SAVED_WORKOUTS_FILE_PATH = "backend/saved_workouts.pckl"


class WorkoutGeneratorUtility:
    latest_workout: Optional[Exercise] = None
    lift_history: List[Exercise] = []

    @classmethod
    def get_excluded_exercises(cls) -> List[Exercise]:
        """
        Gets the excluded exercises based on the lift history's 2 most recent workouts
        Returns:
            List[Exercise]: list of excluded exercises
        """
        look_back_window = []
        excluded_exercises = set()
        if cls.lift_history:
            if len(cls.lift_history) == 1:
                look_back_window = [cls.lift_history[0]]
            else:
                look_back_window = cls.lift_history[-2:]
        for workout in look_back_window:
            for exercise in workout.exercises.values():
                if exercise:
                    excluded_exercises.add(exercise)

        return excluded_exercises

    @staticmethod
    def generate_random_exercise_for_body_part(
        body_part: BodyPart, excluded_exercises: List[Exercise]
    ) -> Exercise:
        """
        Returns a random exercise (excluding excluded exercises).

        Args:
            body_part: body part to generate exercise for.
            excluded_exercises: list of excluded exercises

        Returns:
            Exercise: one of the exercises for a workout
        """
        available_exercises = [
            exercise
            for exercise in LIFTS_BY_BODY_PART[body_part]
            if exercise not in excluded_exercises
        ]
        return random.choice(available_exercises)

    @classmethod
    def generate_workout(cls) -> None:
        # Creates a workout going through each of the body parts for that workout.

        excluded_exercises = cls.get_excluded_exercises()

        workout = LiftWorkout()

        # Select exercises for the current workout, excluding the excluded exercises
        for body_part in LIFTS_BY_BODY_PART:
            exercise = cls.generate_random_exercise_for_body_part(
                body_part=body_part, excluded_exercises=excluded_exercises
            )
            workout.exercises[body_part] = exercise

        cls.latest_workout = workout

    @classmethod
    def load_workouts(cls) -> None:
        # loads historical workouts from FS
        try:
            with open(SAVED_WORKOUTS_FILE_PATH, "rb") as file:
                cls.lift_history = pickle.load(file)
        except FileNotFoundError:
            cls.lift_history = []

    @classmethod
    def save_workout(
        cls,
    ) -> None:
        # saves workout history to FS
        if cls.lift_history is not None and cls.latest_workout is not None:
            cls.lift_history.append(cls.latest_workout)
            with open(SAVED_WORKOUTS_FILE_PATH, "wb") as file:
                pickle.dump(cls.lift_history, file)
                cls.latest_workout = None

    @classmethod
    def get_workout_history(cls) -> List[str]:
        """
        Returns workout history in string format for frontend template.

        Returns:
            List[str]: list of workouts in string form
        """
        return [str(s) for s in cls.lift_history[::-1]]

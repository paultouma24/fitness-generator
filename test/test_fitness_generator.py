import pytest
from fitness_generator import WorkoutGeneratorUtility
from workout_config import BodyPart, Exercise, LiftWorkout


@pytest.mark.parametrize(
    "body_part, excluded_exercises",
    [
        (
            BodyPart.SHRUG,
            [
                Exercise("DB Shrugs", BodyPart.SHRUG),
                Exercise("BB Shrugs", BodyPart.SHRUG),
            ],
        ),
        (
            BodyPart.PRESS,
            [
                Exercise("Seated DB Press", BodyPart.PRESS),
                Exercise("BB Press", BodyPart.PRESS),
            ],
        ),
    ],
)
def test_generate_random_exercise_for_body_part(body_part, excluded_exercises):
    result = WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
        body_part, excluded_exercises
    )
    assert result not in excluded_exercises


def test_generate_workout():
    def mock_historical_workout():
        workout = LiftWorkout()
        workout.exercises = {
            BodyPart.CHEST: WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
                BodyPart.CHEST, ()
            ),
            BodyPart.BACK: WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
                BodyPart.BACK, ()
            ),
            BodyPart.LEGS: WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
                BodyPart.LEGS, ()
            ),
            BodyPart.SHRUG: WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
                BodyPart.SHRUG, ()
            ),
            BodyPart.SHOULDER: WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
                BodyPart.SHOULDER, ()
            ),
            BodyPart.PRESS: WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
                BodyPart.PRESS, ()
            ),
            BodyPart.BICEPS: WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
                BodyPart.BICEPS, ()
            ),
            BodyPart.TRICEPS: WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
                BodyPart.TRICEPS, ()
            ),
            BodyPart.CORE: WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
                BodyPart.CORE, ()
            ),
            BodyPart.CALVES: WorkoutGeneratorUtility.generate_random_exercise_for_body_part(
                BodyPart.CALVES, ()
            ),
        }
        return workout

    most_recent_wokout = mock_historical_workout()
    second_most_recent_workout = mock_historical_workout()

    lift_history = [
        second_most_recent_workout,
        most_recent_wokout,
    ]

    WorkoutGeneratorUtility.lift_history = lift_history

    WorkoutGeneratorUtility.generate_workout()
    new_workout = WorkoutGeneratorUtility.latest_workout

    for ex in new_workout.exercises.values():
        assert ex not in second_most_recent_workout.exercises.values()
        assert ex not in most_recent_wokout.exercises.values()

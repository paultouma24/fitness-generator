from collections import defaultdict
from enum import Enum, auto


class BodyPart(Enum):
    CHEST = auto()
    BACK = auto()
    LEGS = auto()
    SHRUG = auto()  # can be superset with shoulder
    SHOULDER = auto()
    PRESS = auto()
    BICEPS = auto()  # can be superset with biceps
    TRICEPS = auto()
    CORE = auto()  # can be superset with calves
    CALVES = auto()


class Exercise:
    def __init__(
        self,
        name: str,
        body_part: BodyPart,
    ):
        self.name = name
        self.body_part = body_part

    def __str__(self):
        return f"{self.body_part}:{self.name}"

    def __eq__(self, other):
        if isinstance(other, Exercise):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)


class LiftWorkout:  # pylint: disable=too-few-public-methods
    def __init__(self):
        self.exercises = {
            BodyPart.CHEST: None,
            BodyPart.BACK: None,
            BodyPart.LEGS: None,
            BodyPart.SHRUG: None,
            BodyPart.SHOULDER: None,
            BodyPart.PRESS: None,
            BodyPart.BICEPS: None,
            BodyPart.TRICEPS: None,
            BodyPart.CORE: None,
            BodyPart.CALVES: None,
        }

    def __str__(self):
        workout_str = ""
        for body_part, ex in self.exercises.items():
            workout_str += f"{body_part.name}: {ex.name}<br>"
        return workout_str


# instantiate all lift exercises
LIFTING_EXERCISES = [
    # CHEST
    Exercise("Flat DB Press", BodyPart.CHEST),
    Exercise("Flat Barbell Press", BodyPart.CHEST),
    Exercise("Incline DB Press", BodyPart.CHEST),
    Exercise("Incline Barbell Press", BodyPart.CHEST),
    Exercise("Dips", BodyPart.CHEST),
    Exercise("Explosive Push-Ups", BodyPart.CHEST),
    # BACK
    Exercise("Lat Pulldowns", BodyPart.BACK),
    Exercise("Straight Arm Lat Pulldown", BodyPart.BACK),
    Exercise("DB Row", BodyPart.BACK),
    Exercise("Upright Row", BodyPart.BACK),
    Exercise("Pull Up", BodyPart.BACK),
    Exercise("Muscle Up", BodyPart.BACK),
    # LEGS / HINGE
    Exercise("Barbell Front Squat", BodyPart.LEGS),
    Exercise("Glute Bridge", BodyPart.LEGS),
    Exercise("Elevated Slant Board DB Squat", BodyPart.LEGS),
    Exercise("SL DB Lunge", BodyPart.LEGS),
    Exercise("Machine Squat", BodyPart.LEGS),
    Exercise("Machine Leg Extension", BodyPart.LEGS),
    Exercise("Machine Leg Curl", BodyPart.LEGS),
    # SHRUG
    Exercise("DB Shrugs", BodyPart.SHRUG),
    Exercise("BB Shrugs", BodyPart.SHRUG),
    Exercise("Cable Shrugs", BodyPart.SHRUG),
    # PRESS
    Exercise("Seated DB Press", BodyPart.PRESS),
    Exercise("BB Press", BodyPart.PRESS),
    Exercise("Machine Press", BodyPart.PRESS),
    # SHOULDER
    Exercise("DB Lateral Raise", BodyPart.SHOULDER),
    Exercise("Cable Lateral Raise", BodyPart.SHOULDER),
    Exercise("Rear Lateral Raise", BodyPart.SHOULDER),
    # BICEPS
    Exercise("Barbell Curl", BodyPart.BICEPS),
    Exercise("EZ Bar Curl", BodyPart.BICEPS),
    Exercise("Regular DB Curl", BodyPart.BICEPS),
    Exercise("Hammer DB Curl", BodyPart.BICEPS),
    Exercise("Incline Bench DB Curl", BodyPart.BICEPS),
    Exercise("Cable Curl(any attachment)", BodyPart.BICEPS),
    # TRICEPS
    Exercise("Tricep Cable(any attachment)", BodyPart.TRICEPS),
    Exercise("DB Overhead Tricep", BodyPart.TRICEPS),
    Exercise("Seated Tricep EZ Extension", BodyPart.TRICEPS),
    # CORE
    Exercise("Decline Twists", BodyPart.CORE),
    Exercise("Decline Crunch", BodyPart.CORE),
    Exercise("Box and Ball Leg Raises", BodyPart.CORE),
    Exercise("Weighted Hanging Leg Raises", BodyPart.CORE),
    Exercise("Alt Arm/Alt Leg Taps", BodyPart.CORE),
    # CALVES
    Exercise("DB Calf Raise (no stair)", BodyPart.CALVES),
    Exercise("DB Calf Raise (w/ stair)", BodyPart.CALVES),
    Exercise("Unweighted Calf Burnout (disregard reps)", BodyPart.CALVES),
]

# by body part
LIFTS_BY_BODY_PART = defaultdict(list)
for exercise in LIFTING_EXERCISES:
    LIFTS_BY_BODY_PART[exercise.body_part].append(exercise)

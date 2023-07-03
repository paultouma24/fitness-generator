from enum import Enum, auto


class LiftCategory(Enum):
    CHEST = auto()
    BACK = auto()
    HINGE = auto()  # aka legs
    SHRUG = auto()  # can be superset with shoulder
    SHOULDER = auto()
    PRESS = auto()
    BICEPS = auto()
    TRICEPS = auto()
    CORE = auto()  # can be superset with calves
    CALVES = auto()


class LiftExercise:
    def __init__(
        self,
        name: str,
        category: LiftCategory,
    ):
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.category}:{self.name}"


LIFTING_EXERCISES = [
    LiftExercise("Flat DB Press", LiftCategory.CHEST),
    LiftExercise("Flat Barbell Press", LiftCategory.CHEST),
    LiftExercise("Incline DB Press", LiftCategory.CHEST),
    LiftExercise("Incline Barbell Press", LiftCategory.CHEST),
    LiftExercise("Dips", LiftCategory.CHEST),
    LiftExercise("Explosive Push-Ups", LiftCategory.CHEST),
    LiftExercise("Lat Pulldowns", LiftCategory.BACK),
    LiftExercise("Straight Arm Lat Pulldown", LiftCategory.BACK),
    LiftExercise("DB Row", LiftCategory.BACK),
    LiftExercise("Upright Row", LiftCategory.BACK),
    LiftExercise("Pull Up", LiftCategory.BACK),
    LiftExercise("Muscle Up", LiftCategory.BACK),
    LiftExercise("Barbell Front Squat", LiftCategory.HINGE),
    LiftExercise("Glute Bridge", LiftCategory.HINGE),
    LiftExercise("Elevated Slant Board DB Squat", LiftCategory.HINGE),
    LiftExercise("SL DB Lunge", LiftCategory.HINGE),
    LiftExercise("Machine Squat", LiftCategory.HINGE),
    LiftExercise("Machine Leg Extension", LiftCategory.HINGE),
    LiftExercise("Machine Leg Curl", LiftCategory.HINGE),
    LiftExercise("DB Shrugs", LiftCategory.SHRUG),
    LiftExercise("BB Shrugs", LiftCategory.SHRUG),
    LiftExercise("Cable Shrugs", LiftCategory.SHRUG),
    LiftExercise("Seated DB Press", LiftCategory.PRESS),
    LiftExercise("BB Press", LiftCategory.PRESS),
    LiftExercise("Machine Press", LiftCategory.PRESS),
    LiftExercise("DB Lateral Raise", LiftCategory.SHOULDER),
    LiftExercise("Cable Lateral Raise", LiftCategory.SHOULDER),
    LiftExercise("Rear Lateral Raise", LiftCategory.SHOULDER),
    LiftExercise("Barbell Curl", LiftCategory.BICEPS),
    LiftExercise("Regular DB Curl", LiftCategory.BICEPS),
    LiftExercise("Hammer DB Curl", LiftCategory.BICEPS),
    LiftExercise("Incline Bench DB Curl", LiftCategory.BICEPS),
    LiftExercise("Cable Curl(any attachment)", LiftCategory.BICEPS),
    LiftExercise("Tricep Cable(any attachment)", LiftCategory.TRICEPS),
    LiftExercise("DB Overhead Tricep", LiftCategory.TRICEPS),
    LiftExercise("Seated Tricep EZ Extension", LiftCategory.TRICEPS),
    LiftExercise("Decline Twists", LiftCategory.CORE),
    LiftExercise("Decline Crunch", LiftCategory.CORE),
    LiftExercise("Box and Ball Leg Raises", LiftCategory.CORE),
    LiftExercise("Weighted Hanging Leg Raises", LiftCategory.CORE),
    LiftExercise("Alt Arm/Alt Leg Taps", LiftCategory.CORE),
    LiftExercise("DB Calf Raise (no stair)", LiftCategory.CALVES),
    LiftExercise("DB Calf Raise (w/ stair)", LiftCategory.CALVES),
    LiftExercise("Unweighted Calf Burnout (disregard reps)", LiftCategory.CALVES),
]

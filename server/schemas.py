# schemas.py

from marshmallow import Schema, fields, validate

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(validate=validate.Range(min=0))
    sets = fields.Int(validate=validate.Range(min=0))
    duration_seconds = fields.Int(validate=validate.Range(min=0))

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    category = fields.Str(required=True)
    equipment_needed = fields.Bool()
    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema(exclude=("exercise_id",))), dump_only=True)

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(validate=validate.Range(min=1))
    notes = fields.Str()
    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema(exclude=("workout_id",))), dump_only=True)

# Instantiate schemas for easy import in app.py
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True, exclude=("workout_exercises",))

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True, exclude=("workout_exercises",))

workout_exercise_schema = WorkoutExerciseSchema()
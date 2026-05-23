# seed.py

from datetime import date
from app import app
from models import db, Exercise, Workout, WorkoutExercise

with app.app_context():
    print("Clearing out tables...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Seeding Exercises...")
    squat = Exercise(name="Barbell Squat", category="Legs", equipment_needed=True)
    pushup = Exercise(name="Push-up", category="Chest", equipment_needed=False)
    plank = Exercise(name="Plank", category="Core", equipment_needed=False)

    db.session.add_all([squat, pushup, plank])
    db.session.commit()

    print("Seeding Workouts...")
    w1 = Workout(date=date(2023, 10, 1), duration_minutes=45, notes="Leg day focus")
    w2 = Workout(date=date(2023, 10, 3), duration_minutes=30, notes="Quick core and chest")

    db.session.add_all([w1, w2])
    db.session.commit()

    print("Seeding WorkoutExercises (Join Table)...")
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=squat.id, sets=5, reps=5)
    we2 = WorkoutExercise(workout_id=w2.id, exercise_id=pushup.id, sets=3, reps=15)
    we3 = WorkoutExercise(workout_id=w2.id, exercise_id=plank.id, duration_seconds=60)
    
    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("Seed complete!")
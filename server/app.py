# app.py

from flask import Flask, request, jsonify
from flask_migrate import Migrate 
from marshmallow import ValidationError

from models import db, Exercise, Workout, WorkoutExercise
from schemas import (
    exercise_schema, exercises_schema, 
    workout_schema, workouts_schema, 
    workout_exercise_schema
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.errorhandler(ValidationError)
def handle_marshmallow_error(e): 
    return jsonify(e.message), 400

@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workout_schema.dump(workouts)), 200

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return jsonify(workout_schema.dump(workout)), 200

@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    validated_data = workout_schema.load(data)
    
    new_workout = Workout(**validated_data)
    db.session.add(new_workout)
    db.session.commit()
    
    return jsonify(workout_schema.dump(new_workout)), 201

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return jsonify({"message": "Workout deleted"}), 204

@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises)), 200

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    return jsonify(exercise_schema.dump(exercise)), 200

@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()
    validated_data = exercise_schema.load(data)
    
    new_exercise = Exercise(**validated_data)
    db.session.add(new_exercise)
    db.session.commit()
    
    return jsonify(exercise_schema.dump(new_exercise)), 201

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    db.session.delete(exercise)
    db.session.commit()
    return jsonify({"message": "Exercise deleted"}), 204

@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    Workout.query.get_or_404(workout_id)
    Exercise.query.get_or_404(exercise_id)

    data = request.get_json() or {}
    data['workout_id'] = workout_id
    data['exercise_id'] = exercise_id
    
    validated_data = workout_exercise_schema.load(data)
    
    new_we = WorkoutExercise(**validated_data)
    db.session.add(new_we)
    db.session.commit()
    
    return jsonify(workout_exercise_schema.dump(new_we)), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)
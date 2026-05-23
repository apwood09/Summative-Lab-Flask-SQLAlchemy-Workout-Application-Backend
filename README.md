# Flask-SQLAlchemy-Workout Application Backend

A Flask-based RESTful API designed to manage exercise details. This system tracks exercises, cataloged by equipment demands and physiological categories, linking them seamlessly into complete workout histories through relational schemas and performance tracking metrics.

## Project Description

The Exercise Tracker API acts as a structural foundation for fitness applications. The system models physical training parameters through three primary entities:
- **Exercises:** routines or activities tracked by name, physical category, and whether equipment is required.
- **Workouts:** date-stamped sessions that record the duration of the physical training.
- **Workout Exercises (Join Entity):** specialized tracking  capturing parameters like sets, repetitions, or timed step durations.

## Installation Instructions

### 1. Prerequisites
Ensure Python 3.13 installed along with `pipenv`. If you do not have pipenv available globally on your local system, set it up using your global environment's manager:
pip install pipenv

### 2. Initialize Environment & Packages
pipenv install

### 3. Migrate and Seed the Database

# Enter the virtual runtime shell environment
pipenv shell

# Initialize database directory tracks, apply models, and push upgrades
flask db init
flask db migrate -m "Create exercise schema"
flask db upgrade

# Run script to clear outdated tables and seed sample movements
python seed.py

## Run Instructions

### 1. Enter Virtual Space
pipenv shell

### 2. Launch Development API Service
flask run --port=5555

Once initialized, the system runs locally and responds to operations at http://127.0.0.1:5555/


## API Endpoints Reference

### Workout

# /workouts   GET: Fetches a historical catalog summary of all logged physical workout records.

# /workouts/<int:id>   GET: Grabs complete details for a single target workout id, including structural items of all exercises completed.

# /workouts   POST: Sets up a brand new workout record. Enforces data formatting checks for standard dates and durations.

# /workouts/<int:id>   DELETE: Cleanses a specific workout record completely. Automatically drops all linked exercise set entries due to cascade constraints.

### Exercise

# /exercises  GET: Gathers and indexes all global physical movements currently supported by the platform catalog.

# /exercises/<int:id>  GET: Pulls out a specific exercise track detailing equipment constraints and structural labels.

# /exercises  POST:  Registers a fresh entry type into the core tracking catalog. Requires non-empty, original string names.

# /exercises/<int:id>  DELETE: Purges an explicit physical routine choice from the catalog registry. 

### Workout Performance Logs (Join Table)

# /workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises  POST: Bridges an exercise to a given workout plan line-item. Accepts performance specifications like reps, sets, or time in seconds. 

## Pipfile Dependencies

[[source]]
url = "[https://pypi.org/simple](https://pypi.org/simple)"
verify_ssl = true
name = "pypi"

[packages]
flask = "==2.2.2"
flask-sqlalchemy = "==3.0.3"
flask-migrate = "==3.1.0"
werkzeug = "==2.2.2"
marshmallow = "==3.20.1"
importlib-metadata = "==6.0.0"
importlib-resources = "==5.10.0"

[dev-packages]
ipdb = "==0.13.9"

[requires]
python_version = "3.13"
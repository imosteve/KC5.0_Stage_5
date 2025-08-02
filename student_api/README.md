# Task 1: Student Result Management API

**Goal:** Build a FastAPI-based API to manage student scores and compute grades.

### Features:
- Create and manage students with `name`, `subject_scores`, `average`, and `grade`.
- Save student data to `students.json`.
- Handle errors using `try-except`.

### Endpoints:
- `POST /students/`: Add a new student and compute their grade.
- `GET /students/{name}`: Get a specific student’s details.
- `GET /students/`: Retrieve all students.

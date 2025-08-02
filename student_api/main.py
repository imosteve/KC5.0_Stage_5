from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Union
import json
import os

app = FastAPI()

DATA_FILE = "student_api/students.json"
# DATA_FILE = "students.json"

class Student(BaseModel):
    name: str
    subject_scores: Dict[str, float]
    average: float = 0.0
    grade: str = ""


class ResponseModel(BaseModel):
    message: str
    status: bool
    data: Union[Student, List[Student], None]


def calculate_average(scores: Dict[str, float]) -> float:
    return sum(scores.values()) / len(scores)

def calculate_grade(average: float) -> str:
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"

def read_data() -> List[Student]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        students = json.load(f)
        return [Student(**s) for s in students]


def write_data(students: List[Student]):
    with open(DATA_FILE, "w") as f:
        json.dump([s.dict() for s in students], f, indent=4)


@app.post("/students/", response_model=ResponseModel)
def create_student(student: Student):
    try:
        students = read_data()
        for s in students:
            if s.name.lower() == student.name.lower():
                return {
                    "message": "Student already exists",
                    "status": False,
                    "data": None
                    }

        student.average = calculate_average(student.subject_scores)
        student.grade = calculate_grade(student.average)
        students.append(student)
        write_data(students)
        return {
            "message": "Student result added successfully",
            "status": True,
            "data": student
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }


@app.get("/students/{name}", response_model=ResponseModel)
def get_student(name: str):
    try:
        students = read_data()
        for s in students:
            if s.name.lower() == name.lower():
                return {
                    "message": "Successfully fetched",
                    "status": True,
                    "data": s
                }
        return {
            "message": "Student not found",
            "status": False,
            "data": None
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }


@app.get("/students/", response_model=ResponseModel)
def list_students():
    try:
        student_lists = read_data()
        return {
            "message": "students fetched successfully",
            "status": True,
            "data": student_lists
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }

import json
import os
from typing import List
from pydantic import BaseModel

FILE_PATH = "job_app_tracker_api/applications.json"

class JobApplication(BaseModel):
    name: str
    company: str
    position: str
    status: str

def load_applications() -> List[dict]:
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_applications(applications: List[dict]) -> None:
    with open(FILE_PATH, "w") as file:
        json.dump(applications, file, indent=4)

def add_application(application: JobApplication) -> dict:
    applications = load_applications()
    new_application = application.dict()
    applications.append(new_application)
    save_applications(applications)
    return new_application

def list_applications() -> List[dict]:
    return load_applications()

def search_by_status(status: str) -> List[dict]:
    applications = load_applications()
    return [app for app in applications if app["status"].lower() == status.lower()]

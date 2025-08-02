from fastapi import FastAPI, Query
from pydantic import BaseModel
from .file_handler import add_application, list_applications, search_by_status

app = FastAPI()

class JobApplication(BaseModel):
    name: str
    company: str
    position: str
    status: str

@app.post('/applications/')
def create_application(application: JobApplication):
    try:
        added_app = add_application(application)
        return {
            "message": "Application added successfully",
            "status": True,
            "data": added_app
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }

@app.get('/applications/')
def get_applications():
    try:
        applications = list_applications()
        return {
            "message": "Applications fetched successfully",
            "status": True,
            "data": applications
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }

@app.get('/applications/search')
def search_applications(status: str = Query(..., description="Filter applications by status")):
    try:
        results = search_by_status(status)
        return {
            "message": "Applications filtered successfully",
            "status": True,
            "data": results
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }

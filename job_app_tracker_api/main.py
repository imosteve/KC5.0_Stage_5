from fastapi import FastAPI, Query
from .file_handler import JobApplication,add_application, list_applications, search_by_status

app = FastAPI()

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
        if not applications:
            return {
                "message": "No application added",
                "status": False,
                "data": None
            }
        else:
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
        if not results:
            return {
                "message": "Application not found",
                "status": False,
                "data": None
            }
        else:
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

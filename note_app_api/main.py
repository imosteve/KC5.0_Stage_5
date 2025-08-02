from fastapi import FastAPI
from pydantic import BaseModel
from .file_handler import save_note, get_note, update_note, delete_note

app = FastAPI()


class NoteCreate(BaseModel):
    title: str
    content: str

class NoteUpdate(BaseModel):
    new_content: str


@app.post('/notes/')
def create_note(note: NoteCreate):
    try:
        result = save_note(note.title, note.content)
        return {
            "message": "Note created successfully",
            "status": True,
            "data": result
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }


@app.get('/notes/{title}')
def read_note(title: str):
    try:
        content = get_note(title)
        return {
            "message": "Note retrieved successfully",
            "status": True,
            "data": content
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }


@app.post('/notes/{title}')
def modify_note(title: str, note: NoteUpdate):
    try:
        updated = update_note(title, note.new_content)
        return {
            "message": "Note updated successfully",
            "status": True,
            "data": updated
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }


@app.delete('/notes/{title}')
def remove_note(title: str):
    try:
        delete_note(title)
        return {
            "message": "Note deleted successfully",
            "status": True,
            "data": None
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }

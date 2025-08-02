from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, EmailStr
from .contact_handler import add_contact, get_contact, update_contact_phone, update_contact_email

app = FastAPI()


class Contact(BaseModel):
    name: str
    phone: str
    email: EmailStr

@app.post("/contacts/")
def create_contact(contact: Contact):
    try:
        result = add_contact(contact)
        return {
            "message": "Contact created successfully",
            "status": True,
            "data": result
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }

@app.get("/contacts/")
def read_contact(name: str = Query(..., description="Name of the contact")):
    try:
        result = get_contact(name)
        return {
            "message": "Contact retrieved successfully",
            "status": True,
            "data": result
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }

@app.post("/contacts/{name}")
def update_phone(
    name: str = Path(..., description="Name of the contact to update phone"),
    new_phone: str = Query(..., description="New phone number")
):
    try:
        result = update_contact_phone(name, new_phone)
        return {
            "message": "Contact phone updated successfully",
            "status": True,
            "data": result
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }

@app.post("/contacts/{name}/email")
def update_email(
    name: str = Path(..., description="Name of the contact to update email"),
    new_email: EmailStr = Query(..., description="New email address")
):
    try:
        result = update_contact_email(name, new_email)
        return {
            "message": "Contact email updated successfully",
            "status": True,
            "data": result
        }
    except Exception as e:
        return {
            "message": str(e),
            "status": False,
            "data": None
        }

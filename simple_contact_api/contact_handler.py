from typing import Dict
from pydantic import BaseModel, EmailStr


class Contact(BaseModel):
    name: str
    phone: str
    email: EmailStr

contacts_db: Dict[str, Contact] = {}

def add_contact(contact: Contact):
    if contact.name in contacts_db:
        raise ValueError("Contact already exists")
    contacts_db[contact.name] = contact
    return contact

def get_contact(name: str):
    contact = contacts_db.get(name)
    if not contact:
        raise ValueError("Contact not found")
    return contact
 
def update_contact_phone(name: str, new_phone: str):
    contact = contacts_db.get(name)
    if not contact:
        raise ValueError("Contact not found")
    contact.phone = new_phone
    contacts_db[name] = contact
    return contact

def update_contact_email(name: str, new_email: str):
    contact = contacts_db.get(name)
    if not contact:
        raise ValueError("Contact not found")
    contact.email = new_email
    contacts_db[name] = contact
    return contact

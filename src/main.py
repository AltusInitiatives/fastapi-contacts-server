from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Contact(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    tags: list[str] = []

# In-memory storage — module level, not inside a function
contacts_db: dict[int, Contact] = {}
next_id: int = 1

@app.get("/contacts")
def get_all_contacts():
    return list(contacts_db.values())

@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    if contact_id not in contacts_db:
        raise HTTPException(status_code=404, detail=f"Contact {contact_id} not found")
    return contacts_db[contact_id]

@app.post("/contacts", status_code=201)
def create_contact(contact: Contact):
    global next_id
    contact.id = next_id
    contacts_db[next_id] = contact
    next_id += 1
    return contact

@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: Contact):
    if contact_id not in contacts_db:
        raise HTTPException(status_code=404, detail=f"Contact {contact_id} not found")
    contact.id = contact_id
    contacts_db[contact_id] = contact
    return contact

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    if contact_id not in contacts_db:
        raise HTTPException(status_code=404, detail=f"Contact {contact_id} not found")
    del contacts_db[contact_id]
    return {"message": f"Contact {contact_id} deleted successfully"}
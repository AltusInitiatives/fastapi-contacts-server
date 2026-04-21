# FastAPI Contacts Server

A FastAPI Contacts Server Simulation

## Features
- GET /contacts — retrieve all contacts
- GET /contacts/{id} — retrieve a single contact by ID
- POST /contacts — create a new contact (Pydantic-validated)
- PUT /contacts/{id} — update an existing contact
- DELETE /contacts/{id} — remove a contact
- Input validation via Pydantic models
- Auto-generated API docs at /docs (Swagger UI)

## Tech Stack
- Python 3.13
- FastAPI
- Uvicorn
- Pydantic
- uv (package manager)

## Setup
\```bash
git clone https://github.com/AltusInitiatives/fastapi-contacts-server.git
cd fastapi-contacts-server
uv sync
\```

## Usage
\```bash
uv run uvicorn src.main:app --reload
\```
Output is displayed on FastAPI demo page
API available at http://localhost:8000 — interactive docs at http://localhost:8000/docs

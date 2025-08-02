# Task 4: Notes App API (With File System Support)

**Goal:** Create a FastAPI app to add, update, and delete notes saved as text files.

### Features:
- Notes are stored as individual `.txt` files.
- Use the `os` module for file handling.
- Structured with error handling.

### Endpoints:
- `POST /notes/`: Create a new note.
- `GET /notes/{title}`: Read a note by its title.
- `POST /notes/{title}`: Update a note by its title.
- `DELETE /notes/{title}`: Delete a note.

---
# Task 5: Simple Contact API (Using Path & Query Parameters)

**Goal:** Build a FastAPI contact management system using path and query parameters.

### Features:
- Manage contacts with `name`, `phone`, and `email`.
- Data stored in a Python dictionary (in-memory).
- Input validation and graceful error handling.

### Endpoints:
- `POST /contacts/`: Add a new contact.
- `GET /contacts/?name=John`: Search for a contact by name using a query parameter.
- `POST /contacts/{name}`: Update contact details using a path parameter.
- `DELETE /contacts/{name}`: Delete a contact by name.

---
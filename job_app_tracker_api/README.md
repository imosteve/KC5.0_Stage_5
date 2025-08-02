# Task 3: Job Application Tracker API

**Goal:** Build an API to manage and search job applications.

### Features:
- Track job applications with `name`, `company`, `position`, and `status`.
- Store and retrieve applications from `applications.json`.
- Use `file_handler.py` to handle file I/O.
- Gracefully handle invalid inputs.

### Endpoints:
- `POST /applications/`: Add a new job application.
- `GET /applications/`: View all job applications.
- `GET /applications/search?status=pending`: Search applications by status using query parameters.

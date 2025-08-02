import os

NOTES_DIR = "note_app_api/notes"

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def save_note(title: str, content: str):
    file_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if os.path.exists(file_path):
        raise FileExistsError("Note already exists")
    with open(file_path, "w") as file:
        file.write(content)
    return {"title": title, "content": content}

def get_note(title: str):
    file_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(file_path):
        raise FileNotFoundError("Note not found")
    with open(file_path, "r") as file:
        return {"title": title, "content": file.read()}

def update_note(title: str, new_content: str):
    file_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(file_path):
        raise FileNotFoundError("Note not found")
    with open(file_path, "w") as file:
        file.write(new_content)
    return {"title": title, "content": new_content}

def delete_note(title: str):
    file_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(file_path):
        raise FileNotFoundError("Note not found")
    os.remove(file_path)

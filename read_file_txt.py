import json

def list_tasks():
    with open("task.json", "r", encoding="utf-8") as f:
        return json.load(f)

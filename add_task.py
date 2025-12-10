import json

def add_new_task(title,  status):
    print(f'\n Новая таска добавленa \n title:{title}, status:{status}')
    with open("task.json", "r", encoding="utf-8") as file:
        tasks =  json.load(file)
    new_id = tasks[-1]["id"] + 1 if tasks else 1

    new_task = {
        "id":new_id,
        "title": title,
        "status": status
    }

    tasks.append(new_task)
    with open("task.json","w", encoding="utf=8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
from read_file_txt import list_tasks
from add_task import add_new_task
from update import update_file

class Start_todo_list:
    tasks = []

    def __init__(self):
        self.tasks = list_tasks()
        self.view_task()

    # Показ задач
    def view_task(self):
        print("\n--- Ваш Todo List --- \n")
        for task in self.tasks:
            print(f"{task['id']} | {task['title']} | {task['status']} ")
        print("--------------------- \n")
        
        print("Добавить задачу(1) \nУдалить задачу(2) \nОбновить статус задачи(3)")
        while True:
            input_choice = int(input("\nСписок действий:"))
            match input_choice:
                case 1:
                    self.add_task()
                    break
                case 2:
                    id = int(input("Какую задачу вы хотите удалить?(id): "))
                    self.delete_task(id)
                    break
                case 3:
                    id = int(input("Какую задачу вы хотите обновить?(id): "))
                    self.update_status_task(id)
                    break
                case _:
                    print("Такого нету")

    # Удаление задач
    def delete_task(self, id):
        tasks = [task for task in self.tasks if task["id"] != id]
        update_file(tasks)
        print("Успешно удалено")

    def update_status_task(self, id):
        status = bool(int(input(f"Какой вы хотите статус? (1=True, 0=False): ")))
        found  = False

        for task in self.tasks:
            if task["id"] == id:
                task["status"] = status
                found = True
                break
        if not found:
            print("Такого ID нету")
        else:
            update_file(self.tasks)
            print("Статус обновлен")


    def add_task(self):
        print("--- Добавление новой задачи --- \n")
        title   = str(input("Заголовок: "))
        status = bool(int(input("Статус (1=True, 0=False): ")))       
        print("--------------------- \n")
        add_new_task(title, status)



START = Start_todo_list()
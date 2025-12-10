from read_file_txt import read_tasks
from add_task import add_new_task


class Start_todo_list:
    repeat    = True
    tasks = []

    def __init__(self):
        self.repeat    = None
        self.tasks = read_tasks()

        print("Добро пожаловать в To-do list!")
        print("Вам доступно одно из дейсвий: \n")

        print("(1): Показать все таски")
        print("(2): Добавить задачу")
        print("(3): Удалить одну таску")

        while True:
            input_choice = int(input("Введите цифру: "))

            match input_choice:
                case 1:
                    self.view_task()
                    break
                case 2:
                    self.add_task()
                    break
                case 3:
                    self.delete_task()
                    break
                case _:
                    print("Такого нету")

    # Показ задач
    def view_task(self):
        print("\n--- Ваш Todo List --- \n")
        for task in self.tasks:
            print(f"{task['id']} | {task['title']} | {task['status']} ")
        print("\n --------------------- \n")

    # Удаление задач
    def delete_task(self):
        print("Удаление задач")

    def add_task(self):
        print("--- Добавление новой задачи --- \n")
        title   = str(input("Заголовок: "))
        status = bool(int(input("Статус (1=True, 0=False): ")))       
        print("--------------------- \n")
        add_new_task(title, status)



START = Start_todo_list()
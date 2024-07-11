# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, tsk, time, status=False):
        self.tsk = tsk
        self.time = time
        self.status = status

    def mark_as_done(self):
        self.status = True

    def print_tsk(self):
        return f"Задача: {self.tsk}, срок: {self.time}, статус: {'выполнено' if self.status else 'не выполнено'}"

tasks = []

def new_tsk():
    desc = input("Введите описание задачи: ")
    time = input("Введите срок выполнения задачи: ")
    new_task = Task(desc, time)
    tasks.append(new_task)

def print_current_tasks():
    for task in tasks:
        if not task.status:
            print(task.print_tsk())

# Пример использования
new_tsk()  # Добавление новой задачи
new_tsk()  # Добавление еще одной задачи

# Отметка первой задачи как выполненной

tasks[0].mark_as_done()

# Вывод списка текущих (не выполненных) задач
print_current_tasks()
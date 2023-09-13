class TaskManager:
    def __init__(self):
        self.tasks = {} # Simulação de um banco de dados em memória

    def add_task(self, id, description):
        self.tasks[id] = description
        print(f"Task added: {description}")

    def list_tasks(self):
        print("Listing tasks:")
        for id, description in self.tasks.items():
            print(f"ID: {id}, Description: {description}")

    def delete_task(self, id):
        if id in self.tasks:
            del self.tasks[id]
            print(f"Task with ID {id} deleted")
        else:
            print("Task not found")


# Exemplo de uso
if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.add_task(1, "Task 1")
    task_manager.add_task(2, "Task 2")
    task_manager.list_tasks()
    task_manager.delete_task(1)
    task_manager.list_tasks()



Se encarga de gestionar el almacenamiento de los datos en memoria."""

from models.task import Task

class TaskRepository:
    # Simula mi base de datos
    _tasks: list[Task] = [
        Task("Estudiar POO", "Repasar arquitectura por capas"),
        Task("Hacer tarea", "Implementar Treeview en Tkinter"),
    ]

    def __init__(self) -> None:
        pass

    def find_all(self) -> list[Task]:
        """Retorna todas las tareas registradas."""
        return self._tasks

    def create_one(self, task: Task):
        self._tasks.append(task)
"""

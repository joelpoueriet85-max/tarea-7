from repositories.task_repository import TaskRepository
from services.task_service import TaskService
from ui.app_window import AppWindow


def main():
    repository = TaskRepository()
    service = TaskService(repository)

    app_window = AppWindow(service)
    app_window.mainloop()


if __name__ == "__main__":
    main()

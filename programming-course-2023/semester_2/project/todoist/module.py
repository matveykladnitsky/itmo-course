from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.api import TodoistAPI


class TodoistModule:
    def __init__(self, api_token: str):
        self.api = TodoistAPI(api_token)

    def get_tasks_list(self) -> str:
        return self.format_tasks(self.api.get_tasks(filter="сегодня | просрочено"))

    def format_tasks(self, tasks: list) -> str:
        output = "Вам необходимо выполнить следующие задачи:\n"

        for task in tasks:
            output += f"{task.content}\n"

        return output

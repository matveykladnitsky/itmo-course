# @file module.py
#  @brief Модуль для взаимодействия с API Todoist и форматирования задач.
from todoist_api_python.api import TodoistAPI


# @brief Класс для работы с API Todoist и форматирования задач.
class TodoistModule:
    # @brief Конструктор класса TodoistModule.
    #  @param api_token Токен API Todoist.
    def __init__(self, api_token: str):
        self.api = TodoistAPI(api_token)

    # @brief Получает список задач на сегодня и просроченных.
    #  @return Отформатированный список задач.
    def get_tasks_list(self) -> str:
        return self.format_tasks(self.api.get_tasks(filter="сегодня | просрочено"))

    # @brief Форматирует список задач в удобочитаемый вид.
    #  @param tasks Список задач, полученных из API Todoist.
    #  @return Отформатированная строка со списком задач.
    def format_tasks(self, tasks: list) -> str:
        output = "Вам необходимо выполнить следующие задачи:\n"

        for task in tasks:
            output += f"{task.content}\n"

        return output

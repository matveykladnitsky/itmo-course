# Todoist Reminder Bot

Телеграм-бот, который напоминает о задачах из Todoist.

## Установка

1. Установка зависимости:

   ```
   pip install -r requirements.txt
   ```

2. Создайте файл `.env` и добавьте в него токен вашего бота и токен вашего Todoist:

   ```bash
   TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>
   TODOIST_API_TOKEN=<your_todoist_api_token>
   ```

Или установите переменные окружения в вашей операционной системе.

## Запуск

Для запуска бота выполните команду:

```bash
python3 main.py
```

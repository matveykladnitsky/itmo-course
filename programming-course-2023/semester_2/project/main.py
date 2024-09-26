from telegram import Update
from aiohttp import web
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TOKEN, TODOIST_API_TOKEN
from reminder.module import ReminderModule
from todoist.module import TodoistModule
from bot.module import BotModule


async def setup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('/setup', update.effective_user.first_name)
    # Инициализация модулей и запуск напоминаний для пользователя
    reminder_module = ReminderModule(
        app=app,
        taskModule=TodoistModule(TODOIST_API_TOKEN),
        botModule=BotModule(TOKEN),
        user_id=update.effective_user.id)

    reminder_module.setup_jobs()

    await update.message.reply_text(
        f'Напоминания включены! Продуктивного дня :)')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('/start', update.effective_user.first_name)
    await update.message.reply_text(
        f'Добрый день, {update.effective_user.first_name}!')
    await update.message.reply_text(
        f'Я буду напоминать тебе о твоих задачах в Todoist два раза в день. Утром и вечером.')
    await update.message.reply_text(
        f'Для включения напоминаний введите команду /setup')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("setup", setup))


def main():
    app.run_polling()


if __name__ == '__main__':
    main()

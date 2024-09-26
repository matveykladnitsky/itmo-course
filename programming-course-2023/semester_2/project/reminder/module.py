from datetime import time
import pytz
import schedule
import time as time_module
import threading


class ReminderModule:
    timezone = pytz.timezone('Europe/Moscow')
    time_to_send_list = [time(hour=7, minute=0, tzinfo=timezone), time(
        hour=20, minute=05, tzinfo=timezone)]

    def __init__(self, app, taskModule, botModule, user_id: int):
        self.app = app
        self.taskModule = taskModule
        self.botModule = botModule
        self.user_id = user_id

    def collect_tasks(self) -> None:
        return self.taskModule.get_tasks_list()

    def setup_jobs(self) -> None:
        for time_to_send in self.time_to_send_list:
            schedule.every().day.at(time_to_send.strftime("%H:%M")).do(
                self.broadcast_tasks)

        self.run_scheduler()

    def run_scheduler(self) -> None:
        scheduler_thread = threading.Thread(target=self._run_scheduler)
        scheduler_thread.daemon = True
        scheduler_thread.start()

    def _run_scheduler(self) -> None:
        while True:
            schedule.run_pending()
            time_module.sleep(1)

    def broadcast_tasks(self) -> None:
        print('broadcast_tasks')
        message = self.collect_tasks()
        self.botModule.send_message(self.user_id, message)

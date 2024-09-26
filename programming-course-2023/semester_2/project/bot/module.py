import requests


class BotModule:
    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def send_message(self, chat_id, text):
        method = "sendMessage"
        url = f"{self.api_url}{method}"
        data = {
            "chat_id": chat_id,
            "text": text
        }
        response = requests.post(url, data=data)
        return response.json()

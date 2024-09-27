"""!
@file module.py
@brief Модуль для работы с Telegram Bot API.
"""

import requests


class BotModule:
    """!
    @brief Класс для взаимодействия с Telegram Bot API.
    """

    def __init__(self, token):
        """!
        @brief Инициализирует экземпляр BotModule.
        @param token Токен Telegram-бота.
        """
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def send_message(self, chat_id, text):
        """!
        @brief Отправляет сообщение в указанный чат.
        @param chat_id ID чата, в который нужно отправить сообщение.
        @param text Текст сообщения.
        @return JSON-ответ от Telegram API.
        """
        method = "sendMessage"
        url = f"{self.api_url}{method}"
        data = {
            "chat_id": chat_id,
            "text": text
        }
        response = requests.post(url, data=data)
        return response.json()

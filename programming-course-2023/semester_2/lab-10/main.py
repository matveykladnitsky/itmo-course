import requests
import pyttsx3
import pyaudio
import random
from vosk import Model, KaldiRecognizer

model = Model("data/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

engine = pyttsx3.init()


def get_character_data(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None


def speak(text):
    engine.say(text)
    engine.runAndWait()


def recognize_speech():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1,
                    rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    while True:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            return result[14:-3]  # Удаляем лишний шум


def main():
    speak("Hello, My name is Alice but not from Yandex. I have these four commands: random, save, id, gender. What do you want?")

    while True:
        command = recognize_speech().lower()
        print(f"распознанная команда пользователя: {command}")

        if "random" in command:
            character_id = random.randint(1, 826)
            character = get_character_data(character_id)
            if character:
                speak(f"Character name is {character['name']}")
            else:
                speak("Oopsie, something went wrong")

        elif "save" in command:
            character_id = random.randint(1, 826)
            character = get_character_data(character_id)
            if character:
                image_url = character['image']
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(f"{character['name']}.jpg", "wb") as f:
                        f.write(response.content)
                    speak(f"Image of {character['name']} has been saved.")
                else:
                    speak("No image was saved because of some error")
            else:
                speak("Oopsie, something went wrong")

        elif "id" in command:
            character_id = random.randint(1, 826)
            character = get_character_data(character_id)
            if character:
                speak(f"The ID of {character['name']} is {character['id']}")
            else:
                speak("Oopsie, something went wrong")

        elif "gender" in command:
            character_id = random.randint(1, 826)
            character = get_character_data(character_id)
            if character:
                speak(
                    f"The gender of {character['name']} is {character['gender']}")
            else:
                speak("Oopsie, something went wrong")

        elif "exit" in command or "quit" in command:
            speak("Poka!")
            break

        else:
            speak("I dont understand.")


if __name__ == "__main__":
    main()

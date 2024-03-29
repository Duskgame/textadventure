import playsound
from openai import OpenAI


class ChatGpt:

    def __init__(self, role: str):
        self.verlauf = [{"role": "system", "content": role}]
        self.client = OpenAI()

    def start(self):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.verlauf
        )
        self.verlauf.append(response.choices[0].message)
        return response.choices[0].message.content

    def post(self, user_input: str) -> str:
        message = {"role": "user", "content": user_input}
        self.verlauf.append(message)
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.verlauf
        )
        self.verlauf.append(response.choices[0].message)
        return response.choices[0].message.content

    def play_sound(self, text):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="echo",
            input=text
        )

        response.stream_to_file("output.mp3")
        playsound.playsound("output.mp3", False)

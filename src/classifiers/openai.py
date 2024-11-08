from werkzeug.datastructures import FileStorage
from openai import AsyncOpenAI
from decouple import config


class OpenAIClassifier:
    def __init__(self, file: FileStorage):
        """Classify a file using ChatGPT."""
        self.file = file

    @staticmethod
    def parse_file(file: FileStorage):
        """Parse the file and return the contents."""
        return file.read().decode("utf-8")

    async def classify(self):
        """Classify the file using OpenAI's GPT-4o model."""

        file_contents = self.parse_file(self.file)

        completion = await AsyncOpenAI(
            api_key=config("OPEN_AI_API_KEY")
        ).chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Classify this file"},
                {"role": "user", "content": file_contents},
            ],
        )

        return completion.choices[0].message.content

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class ResearchAgent:
    """Generates research-oriented responses using a Groq LLM."""

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        self.model = os.getenv("GROQ_MODEL")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        if not self.model:
            raise ValueError("GROQ_MODEL not found in .env")

        self.client = Groq(api_key=api_key)

    def research(self, user_query: str, category: str) -> str:
        """Generate a response based on the query category."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are the Research Agent in a multi-agent AI system. "
                        "Answer the user's query clearly and accurately. "
                        "Use headings or bullet points when helpful. "
                        "Do not invent sources or claim that you searched "
                        "the internet when you did not. "
                        f"The query category is: {category}."
                    ),
                },
                {
                    "role": "user",
                    "content": user_query,
                },
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()
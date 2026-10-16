import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class TriageAgent:
    """Classifies user queries using a Groq-powered LLM."""

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.client = Groq(api_key=api_key)

        # Read the model ID from .env so we can keep using
        # the Qwen model that already works for you.
        self.model = os.getenv("GROQ_MODEL")

        if not self.model:
            raise ValueError(
                "GROQ_MODEL not found in .env. "
                "Add the working Qwen model ID."
            )

    def classify(self, user_query: str) -> str:
        """Classify the query into a supported category."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Triage Agent in a multi-agent AI system. "
                        "Classify the user's query into exactly one category: "
                        "technical, research, coding, or general. "
                        "Return only the category name."
                    ),
                },
                {
                    "role": "user",
                    "content": user_query,
                },
            ],
            temperature=0,
        )

        category = response.choices[0].message.content.strip().lower()

        allowed_categories = {
            "technical",
            "research",
            "coding",
            "general",
        }

        if category not in allowed_categories:
            return "general"

        return category
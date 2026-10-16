import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class ResponseAgent:
    """Refines a draft response using a Groq-powered LLM."""

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        self.model = os.getenv("GROQ_MODEL")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        if not self.model:
            raise ValueError("GROQ_MODEL not found in .env")

        self.client = Groq(api_key=api_key)

    def format_response(
        self,
        user_query: str,
        draft_answer: str,
        category: str,
    ) -> str:
        """Turn the research draft into a polished final answer."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are the Response Agent in a multi-agent AI system. "
                        "Improve the clarity, organization, and readability "
                        "of the supplied draft. Preserve its key facts. "
                        "Do not introduce unsupported claims. "
                        "Use headings and bullet points when useful. "
                        "Return only the final answer."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Original query: {user_query}\n"
                        f"Category: {category}\n\n"
                        f"Research draft:\n{draft_answer}"
                    ),
                },
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content.strip()
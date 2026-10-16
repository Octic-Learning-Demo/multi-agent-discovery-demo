from agents.triage_agent import TriageAgent
from agents.research_agent import ResearchAgent
from agents.response_agent import ResponseAgent


class MultiAgentAssistant:
    """Coordinates the three AI agents."""

    def __init__(self):
        self.triage_agent = TriageAgent()
        self.research_agent = ResearchAgent()
        self.response_agent = ResponseAgent()

    def run(self, user_query: str) -> str:
        # Step 1: Classify the query
        print("\n[1/3] Triage Agent is classifying the query...")

        category = self.triage_agent.classify(user_query)

        print(f"      Detected category: {category}")

        # Step 2: Generate a draft answer
        print("\n[2/3] Research Agent is generating an answer...")

        draft_answer = self.research_agent.research(
            user_query=user_query,
            category=category,
        )

        print("      Draft answer generated.")

        # Step 3: Refine the answer
        print("\n[3/3] Response Agent is refining the answer...")

        final_answer = self.response_agent.format_response(
            user_query=user_query,
            draft_answer=draft_answer,
            category=category,
        )

        return final_answer


def main():
    assistant = MultiAgentAssistant()

    print("=" * 55)
    print("       MULTI-AGENT AI ASSISTANT")
    print("             Powered by Groq")
    print("=" * 55)

    while True:
        user_query = input(
            "\nEnter your question (or type 'exit' to quit): "
        ).strip()

        if user_query.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_query:
            print("Please enter a question.")
            continue

        try:
            answer = assistant.run(user_query)

            print("\n" + "=" * 55)
            print("FINAL ANSWER")
            print("=" * 55)
            print(answer)

        except Exception as error:
            print(f"\nAn error occurred: {error}")


if __name__ == "__main__":
    main()
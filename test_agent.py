
from pprint import pprint

from llm_agent import generate_analysis


def main():
    print("=" * 50)
    print("PROOF-CARRYING DATA ANALYST")
    print("AI AGENT TEST")
    print("=" * 50)

    # Example schema describing the available dataset
    schema = {
        "sales": {
            "order_id": "integer",
            "product_name": "string",
            "quantity": "integer",
            "unit_price": "float"
        }
    }

    # Question asked by the user
    question = "Which product performed the best?"

    print("\nAvailable columns:")
    pprint(schema)

    print("\nUser question:")
    print(question)

    print("\nSending question to AI agent...")
    print("Please wait...\n")

    try:
        answer = generate_analysis(question, schema)

        print("=" * 50)
        print("AI AGENT RESPONSE")
        print("=" * 50)

        print("\nStatus:")
        print(answer.get("status", "Unknown"))

        print("\nAnalysis plan:")
        for step in answer.get("plan", []):
            print(f"- {step}")

        print("\nAssumptions:")
        for assumption in answer.get("assumptions", []):
            print(f"- {assumption}")

        print("\nMessage:")
        print(answer.get("message", "No message provided"))

        if answer.get("status") == "ready":
            print("\nProposed Python code:")
            print("-" * 50)
            print(answer.get("code", ""))

        print("\n" + "=" * 50)
        print("AI AGENT TEST COMPLETED")
        print("=" * 50)

    except Exception as error:
        print("\nAI AGENT FAILED")
        print("Error type:", type(error).__name__)
        print("Error details:", str(error))


if __name__ == "__main__":
    main()

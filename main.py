from langchain_core.messages import HumanMessage, HumnanMessage
from langchain_google_genai import ChatGoogleGenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
def main():
    model = ChatGoogleGenAI(
        model="gemini-1.5-flash",
        temperature=0,
    )
    tool = []
    agent = create_react_agent(model=model, tools=tool)
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    print("Lets preform calculations, answer questions, and more!")
    user_input = input("\nYou: ").strip()

    while True:

        if user_input == "exit":
            break

        print("\nAssistant: ", end="")
        for chunk in agent.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")

    
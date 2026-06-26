from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv


load_dotenv()

@tool
def calculator(a: float, b: float, operation: str) -> str:
    """Perform basic arithmetic operations on two numbers.
    
    Args:
        a: The first number.
        b: The second number.
        operation: The math operation to perform. Must be one of: 'add', 'subtract', 'multiply', 'divide'.
    """
    print(f"Tool has been called by agent for operation: {operation}")
    
    operation = operation.lower().strip()
    print("tool received operation:", operation)
    if operation == "add":
        return str(a + b)
    elif operation == "subtract":
        return str(a - b)
    elif operation == "multiply":
        return str(a * b)
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero is undefined."
        return str(a / b)
    else:
        return f"Error: Unknown operation '{operation}'."


def main():

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )
    
    tools = [calculator]
    agent_executor = create_react_agent(model=model, tools=tools)
    
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    print("Lets perform calculations, answer questions, and more!")
    
    while True:
    

        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
            
        if not user_input:
            continue

        print("\nAssistant: ", end="")
        

        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    # Print the content chunks dynamically
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
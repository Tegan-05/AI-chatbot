# AI Chatbot 

A lightweight, local command-line interface (CLI) conversational AI assistant built using Python, LangChain, and LangGraph. The chatbot leverages the powerful Google Gemini API (`gemini-2.5-flash`) for natural language understanding and text generation, structured as an intelligent ReAct (Reasoning and Action) agent capable of utilizing functional tools to execute tasks dynamically.

##  Features

* **Continuous Conversation Loop:** Interactive CLI loop that prompts for user inputs, monitors for termination triggers, and maintains session context dynamically.
* **Agentic Framework:** Leverages `langgraph.prebuilt.create_react_agent` to construct an architecture capable of deciding when to chat and when to call functional tools.
* **Extensible Tool System:** Built-in modular math/calculator functionality designed to handle arithmetic constraints natively.
* **Dynamic Response Streaming:** Streams tokens and messaging updates back to the console in real-time as chunks are received from the API.
* **Secure Credential Auditing:** Built-in environment variable configuration isolated completely from local source history.

## Tech Stack

* **Language:** Python (v3.12+)
* **Orchestration Engine:** LangGraph & LangChain Core
* **LLM Provider:** Google Gemini API (`gemini-2.5-flash` via `langchain-google-genai`)
* **Package Manager:** `uv` by Astral (Fast, reliable Python packaging)
* **Environment Setup:** `python-dotenv`

---

## Installation & Setup

Ensure you have Python 3.12+ and `uv` installed on your machine.

### 1. Clone & Navigate to Repository
```bash
git clone [https://github.com/Tegan-05/AI-chatbot.git](https://github.com/Tegan-05/AI-chatbot.git)
cd "AI-chatbot"

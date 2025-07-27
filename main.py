import os
from langchain_google_genai import ChatGoogleGenerativeAI
from windows_use.agent import Agent
from dotenv import load_dotenv

# Developer tag
print("="*60)
print("🔍  AI AGENT by Nick".center(60))
print("="*60)

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

agent = Agent(llm=llm, use_vision=False)

# Prewarm (optional)
_ = llm.invoke("Hello!")

query = input("Enter your query: ")
agent_result = agent.invoke(query=query)
print("\n📢 Result:")
print(agent_result.content)

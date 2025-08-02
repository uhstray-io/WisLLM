from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph

import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

response = llm.invoke("Say hello and confirm you're working")

print(f"Response: {response.content}")
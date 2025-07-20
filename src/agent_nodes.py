from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # Or "llama3-70b-8192"
    temperature=0,
    groq_api_key=GROQ_API_KEY
)

def planner_node(topic: str):
    prompt = f"Create a detailed research plan for the topic: {topic}"
    response = llm.invoke(prompt)
    return response.content

def searcher_node(topic: str):
    prompt = f"List key points, facts, or findings about the topic: {topic}. Return as bullet points."
    response = llm.invoke(prompt)
    return response.content.split("\n")

def summarizer_node(text: str):
    summary_prompt = f"Summarize the following research content:\n{text}"
    summary_response = llm.invoke(summary_prompt)

    confidence_prompt = (
        f"On a scale from 0 to 100, how confident are you in the factual accuracy "
        f"and completeness of the following summary? Return only a number.\n\n{summary_response.content}"
    )
    confidence_response = llm.invoke(confidence_prompt)

    try:
        confidence_value = int(''.join(filter(str.isdigit, confidence_response.content))) / 100
    except:
        confidence_value = 0.5  # default if parsing fails

    return summary_response.content, confidence_value




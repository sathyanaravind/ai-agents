from agno.agent import Agent
#from agno.models.openai import OpenAI 
from agno.models.groq import Groq 
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv 
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = Agent(
    model=Groq(id="qwen-2.5-32b"),
    description="You are an AI assistant. Please answer the question from the prompts",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("Who defeated psg in champians league round of 16, 2025? ")
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq 
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv 
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="qwen-2.5-32b"),
    description="search the web for information",
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    model=OpenAIChat(id="gpt-4o"),
    description="Get financial data",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_info=True)],
    instructions="use tables to display data",
    show_tool_calls=True,
    markdown=True
)

team_agent = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="qwen-2.5-32b"),
    instructions=["Always include the sources","Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)
team_agent.print_response("What is the best stock for beginner to invest? ")
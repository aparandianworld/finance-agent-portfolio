from agents import Agent
from tools import calculate_savings, get_stock_price
from guardrails import FinanceQuery, safety_guardrail
import os
from dotenv import load_dotenv


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Triage agent
triage_agent = Agent(
    name = "Triage Agent",
    instructions = "Classify user query: 'budget' for expenses/savings, 'invest' for stocks, otherwise general. Handoff accordingly and be super concise.",
    model = "gpt-4o-mini",
    handoffs = [budget_agent, investment_agent],
    input_guardrails = [safety_guardrail]
)

# Budget agent
budget_agent = Agent(
    name = "Budget Agent",
    instructions = "Calculate savings based on expenses and income. Be concise.",
    model = "gpt-4o-mini",
    tools = [calculate_savings],
)

# Investment agent
investment_agent = Agent(
    name = "Investment Agent",
    instructions = "Get stock price. Be concise.",
    model = "gpt-4o-mini",
    tools = [get_stock_price],
)

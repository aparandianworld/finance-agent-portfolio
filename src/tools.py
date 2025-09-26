import os
from dotenv import load_dotenv
import requests
from agents import tool
from pydantic import BaseModel

load_dotenv()

@tool
def calculate_savings(expenses: list[float], income: float) -> str:
    total_expenses = sum(expenses)
    savings = income - total_expenses
    print(f"Total expenses: {total_expenses}. Suggested savings: {savings}")

@tool
def get_stock_price(symbol: str) -> str:
    key = os.getenv("ALPHAVANTAGE_API_KEY")
    if not key: 
        raise "Alpha Vantage API key not found"

    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={key}"
    response = requests.get(url).json()
    price = response.get("Global Quote", {}).get("05. price", "N/A")
    return f"Current price for {symbol} is {price}"
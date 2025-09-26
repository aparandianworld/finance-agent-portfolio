import os
from dotenv import load_dotenv
import requests
from agents import tool
from pydantic import BaseModel

load_dotenv()

@tool
def calculate_savings(expenses: list[float], income: float) -> str:
    try:
        if not expenses or not income:
            raise ValueError("No Expenses and/or income provided")
        if income < 0:
            raise ValueError("Income must be a positive number")
        if any(expense < 0 for expense in expenses):
            raise ValueError("Expenses must be positive numbers")

        total_expenses = sum(expenses)
        savings = income - total_expenses
        print(f"Total expenses: {total_expenses}. Suggested savings: {savings}")

    except Exception as ex:
        return f"Error in calculating savings: {str(ex)}"

@tool
def get_stock_price(symbol: str) -> str:
    try:
        key = os.getenv("ALPHAVANTAGE_API_KEY")
        if not key:
            raise ValueError("Alpha Vantage API key not found")

        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={key}"
        response = requests.get(url, timeout=10).json()
        price = response.get("Global Quote", {}).get("05. price", "N/A")
        return f"Current price for {symbol} is {price}"

    except Exception as ex:
        return f"Error in getting stock price: {str(ex)}"
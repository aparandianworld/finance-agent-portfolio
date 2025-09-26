import os
from dotenv import load_dotenv
import requests

load_dotenv()

def calculate_savings(expenses: list[float], income: float) -> str:
    total_expenses = sum(expenses)
    savings = income - total_expenses
    return f"Total expenses: {total_expenses}. Suggested savings: {savings}"

def get_stock_price(symbol: str) -> str:
    key = os.getenv("ALPHA_VANTAGE_KEY")
    if not key:
        raise "Alpha Vantage API key not found"

    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={key}"
    response = requests.get(url).json()
    price = response.get("Global Quote", {}).get("05. price", "N/A")
    return f"Current price for {symbol} is {price}"

def test_tools():
    print("===Testing calculate_budget===")
    expenses = [1000.0, 800.0, 1200.0]
    income = 5000.0
    result = calculate_savings(expenses, income)
    print(result, end = "")

    print("\n===Testing get_stock_price===")
    symbol = "AAPL"
    result = get_stock_price(symbol)
    print(result)

if __name__ == "__main__":
    test_tools()
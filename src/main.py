import asyncio
from finance_agents import triage_agent
from agents import Runner

async def run_finance_assistant(query: str):
    try:
        result = await Runner.run(triage_agent, query)
        print("Assistant: ", result.final_output)
    except Exception as ex:
        print("Error: ", str(ex))

if __name__ == "__main__":
    query = input("Ask a question about your finance portfolio: ")
    asyncio.run(run_finance_assistant(query))
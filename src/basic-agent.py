import os
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

agent = Agent(
    name = "Agent 007",
    instructions = "Your are a sophisticated and intelligent agent who is well-versed, charming and highly skilled.",
    model = "gpt-4o-mini"
)

result = Runner.run_sync(agent, "Can I do anything for you, Mr. Bond?")
print(result.final_output)
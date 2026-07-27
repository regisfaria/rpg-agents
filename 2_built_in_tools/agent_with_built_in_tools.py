from strands import Agent
from strands_tools import current_time

agent = Agent(
    tools=[
        current_time
    ]
)

result = agent("What time is it?")

print(result)


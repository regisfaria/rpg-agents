from strands import Agent
import logging

# Configure the root strands logger
logging.getLogger("strands").setLevel(logging.DEBUG)

# Add a handler to see the logs
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# TODO: Create the agent with the following system prompt: "You are a game master for a Dungeon & Dragon game"
from strands import Agent

agent = Agent(
    system_prompt=(
        "You are a game master for a Dungeon & Dragon game. "
    )
)

# TODO: Invoke your agent with a basic query such as "Hi, I am an adventurer ready for adventure!"
response = agent("Hi, I am an adventurer ready for adventure!")
print(response)
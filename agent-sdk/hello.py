import requests
from dotenv import load_dotenv
from agents import Agent, Runner, WebSearchTool, function_tool

load_dotenv()


@function_tool()
def get_weather(city: str):
    """Fetch the weather for a given city name.
    Args:
        city: The city name to fetch the waether for
    """

    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"


hello_agent = Agent(
    name="Hello World Agent",
    instructions="You are an agent which greets the user politely and in a funny way",
    tools=[
        # WebSearchTool(), # Hosted tool
        get_weather
    ],
)

result = Runner.run_sync(hello_agent, "Hey What's the weather of delhi 110027 today")
print(result.final_output)

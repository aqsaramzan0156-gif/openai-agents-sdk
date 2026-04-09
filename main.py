# # import asyncio

# # async def main():
# #     print('Hello ...')
# #     await asyncio.sleep(1)
# #     print('... World!')

# # asyncio.run(main()) 

import asyncio
from openai import AsyncOpenAI
from agents import (
    Agent, Runner, 
    function_tool, 
    OpenAIChatCompletionsModel
)
from agents.tracing import set_tracing_disabled

set_tracing_disabled(True)


model = OpenAIChatCompletionsModel(
    model="minimax-m2:cloud",  
    openai_client=AsyncOpenAI(
        api_key="ollama",  
        base_url="http://localhost:11434/v1"
    )
)


history_agent = Agent(
    model=model,  
    name="History Tutor",
    instructions="You answer history questions clearly and concisely"
)

async def main():
    query = "who built badshahi masjid in lahore pakistan"
    result = await Runner.run(history_agent, query) 
    print(result.final_output) 

if __name__ == "__main__":
    asyncio.run(main()) 



   




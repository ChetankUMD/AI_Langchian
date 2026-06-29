from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool
from langchain.messages import HumanMessage, ToolMessage, AIMessage

load_dotenv()
model = ChatOpenAI(model='gpt-5.4-mini')
message = "Can you multiply 34 and 60?"

class Multiply(BaseModel):
    a: int = Field(description="First number to multiply")
    b: int = Field(description="Second number to multiply")

def multiply(a: int, b: int) -> int:
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    name='Multiply',
    description= "Multiply two numbers",
    args_schema=Multiply
)
chat_history = []

llm_with_tool = model.bind_tools([multiply_tool])

query = HumanMessage(message)
chat_history.append(query)

result_tool = llm_with_tool.invoke(chat_history)
chat_history.append(result_tool)

tool_result = multiply_tool.invoke(result_tool.tool_calls[0])
chat_history.append(tool_result)

result = llm_with_tool.invoke(chat_history)

print(result.content)
print(chat_history)




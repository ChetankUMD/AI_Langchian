from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini')

parser = JsonOutputParser()

class Topic(BaseModel):
    name: str = Field(description="name of the topic")
    facts: list[str] = Field(description="List of fact s about the topcis", min_length=2, max_length=3)

parser = JsonOutputParser(pydantic_object=Topic)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write facts on the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# print(template1)
chain = template1 | model | parser

result = chain.invoke({'topic': 'Oceans'})

print(len(result['facts']))
print(result)


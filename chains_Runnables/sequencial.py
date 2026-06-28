from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import BaseModel, Field


load_dotenv()
model = ChatOpenAI(model='gpt-4o-mini')

class Topic(BaseModel):
    name: str = Field(description="name of the topic")
    facts: list[str] = Field(description="List of fact s about the topcis", min_length=2, max_length=3)

class Report(BaseModel):
    report: str = Field(description="Complete report on the topic")

parser1 = JsonOutputParser(pydantic_object=Report)
parser2 = JsonOutputParser(pydantic_object=Topic)


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed on the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser1.get_format_instructions()}
)

template2 = PromptTemplate(
    template='Extract the facts from {report} \n {format_instruction}',
    input_variables=['report'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

# print(template1)
chain = template1 | model | parser1 | template2 | model | parser2 

result = chain.invoke({'topic': 'Oceans'})

print(len(result['facts']))
# print(result)


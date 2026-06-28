from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

class TopicFacts(BaseModel):
    fact_1: str = Field(description='Fact 1 about the topic')
    fact_2: str = Field(description='Fact 2 about the topic')

parser = JsonOutputParser(pydantic_object=TopicFacts)

template1 = PromptTemplate(
    template='Write a detailed report on {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template1 | model | parser

result = chain.invoke({'topic': 'Oceans'})

print(result)

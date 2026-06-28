from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template1 | model | parser

result = chain.invoke({'topic': 'Oceans'})

print(result)


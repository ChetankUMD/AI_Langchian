from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()
model = ChatOpenAI(model='gpt-4o-mini')

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="This is the sentiment of the feedback")

parser_feedback = JsonOutputParser(pydantic_object=Feedback)
parser_string = StrOutputParser()

prompt_input = PromptTemplate(
    template = "Generate a sentiment of the feedback /n {text} /n {format_instruction}",
    input_variables = ['text'],
    partial_variables={'format_instruction': parser_feedback.get_format_instructions()}
)

prompt_positive = PromptTemplate(
    template = "Give very brief response to postive feedback",
    input_variables = [],
)

prompt_negative = PromptTemplate(
    template = "Give very brief response to negative feedback /n",
    input_variables = [],
)

classifer_chain = prompt_input | model | parser_feedback

branching_chain = RunnableBranch(
    (lambda x: x['sentiment'] == 'positive', prompt_positive | model | parser_string),
    (lambda x: x['sentiment'] == 'negative', prompt_negative | model | parser_string),
    RunnableLambda(lambda x: "Sorry, couldn't get the sentiment behind the feedback")
)

chain = classifer_chain | branching_chain

print(chain.invoke({'text': 'Phone works wonderful'}))

chain.get_graph().print_ascii()
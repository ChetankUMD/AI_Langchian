from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model='gpt-4o-mini')

str_parser = StrOutputParser()

joke_creater_prompt = PromptTemplate(
    template='Generate one joke about women',
    input_variables=[]
)

create_joke_chain = joke_creater_prompt | model | str_parser

parllel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'number_of_words': RunnableLambda(lambda x:len(x.split()))
})

chain = create_joke_chain | parllel_chain
result = chain.invoke({})

print(result['joke'])
print(result['numbers_of_words'])

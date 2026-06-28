from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-5.4-mini')

result = llm.invoke("what is one batmans famous line?")

print(result.content)
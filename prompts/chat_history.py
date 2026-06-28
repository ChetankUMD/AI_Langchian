from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model='gpt-5.4-mini')

docs = [
    HumanMessage(content="Tell me about oceans"),
    AIMessage(content="Ocnes are the sea where water is salty")
]

chat_template = ChatPromptTemplate([
    ('system', 'Your a very good assistant, who answer question on {topic}'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []

for chat in docs:
    chat_history.append(chat)

while True:
    user_query = input("You : ")
    chat_history.append(HumanMessage(content=user_query))
    prompt = chat_template.invoke({'chat_history':chat_history, 'topic': 'oceans','query':user_query})
    if user_query == 'exit':
        break
    result = model.invoke(prompt)
    chat_history.append(AIMessage(content=result.content))
    print(result.content)

print(chat_history)


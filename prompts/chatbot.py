from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-5.4-mini')

chat_history = []
chat_history.append(SystemMessage(content="Your are a idiot who always gives wrong answers"))
while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input == "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(result.content)

print(chat_history)






# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI(model='gpt-5.4-mini')

# chat_history = []
# while True:
#     user_input = input("You : ")
#     chat_history.append(user_input)

#     if user_input == "exit":
#         break

#     result = model.invoke(chat_history)
#     output = f"AI: {result.content}"
#     chat_history.append(output)
#     print(chat_history)
#     print(output)
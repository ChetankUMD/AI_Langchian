from typing import TypedDict, Annotated, Optional
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model='gpt-5.4-mini')

class OnboardingResponse(TypedDict):
    summary: Annotated[str, "Summry why the paitent is coming to therapy"]
    main_concerns: Annotated[list[str], "Give me maximum two points on why the patient want to come to therapy"]
    primary_concerns: Annotated[list[str], "Give me somthing like example: Anxity, depression etc with respect to the paitent onboarding text"]
    name: Annotated[Optional[str], "Name of the paitent"]



strutured_model = model.with_structured_output(OnboardingResponse)

user_input = """Honestly, I've just been feeling really overwhelmed lately. Like, I wake up and already feel behind on everything. My anxiety has been through the roof and I don't really know how to manage it on my own anymore."""

response = strutured_model.invoke(user_input)

print(response)

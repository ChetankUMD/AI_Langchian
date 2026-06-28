from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()
model = ChatOpenAI(model='gpt-5.4-mini')


class OnboardingResponse(BaseModel):
    summary: str = Field(description="Summry why the paitent is coming to therapy")
    main_concerns: list[str] = Field(description="Give me maximum two points on why the patient want to come to therapy")
    primary_concerns: list[str] = Field(description="Give me somthing like example: Anxity, depression etc with respect to the paitent onboarding text")
    name: Optional[str] = Field(default=None, max_length=20, description="Name of the paitent", examples="Amith")



strutured_model = model.with_structured_output(OnboardingResponse)

user_input = """My name is Chetan Kumar. Honestly, I've just been feeling really overwhelmed lately. Like, I wake up and already feel behind on everything. My anxiety has been through the roof and I don't really know how to manage it on my own anymore."""

response = strutured_model.invoke(user_input)

print(response.name)

from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun().invoke('new on iran war')

print(search)
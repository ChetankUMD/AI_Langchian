from langchain_community.document_loaders import WebBaseLoader


url = "https://www.linkedin.com/in/bentzou/"

load = WebBaseLoader(url)
web_content = load.load()

print(web_content[0].metadata)
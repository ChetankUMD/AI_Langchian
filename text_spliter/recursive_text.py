from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader('Nelson.pdf')

docs = loader.load()

spliter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=10
)

result = spliter.split_documents(docs)

print(result[0])
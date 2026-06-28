from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader('Nelson.pdf')

docs = loader.load()

spliter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=10,
    separator=''
)

result = spliter.split_documents(docs)

print(result[0])
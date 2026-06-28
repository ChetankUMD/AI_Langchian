from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

# embed = embedding.embed_query("Chetan is the Batman in DC movies.")
# print(str(embed))

doc = ["CHetan is the batman in DC movies",
"vamshi is spiderman in marval",
"pavan is the superman in DC",
"Bhumika is wonder woman in DC"]

docs_embed = embedding.embed_documents(doc)
# print(str(docs_embed))


query = "Who is Chetan?"
query_embed = embedding.embed_query(query)

scores = cosine_similarity([query_embed], docs_embed)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(doc[index])
print(f"Similarity score is {score}")








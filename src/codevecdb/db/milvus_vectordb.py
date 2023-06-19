from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Milvus
from tenacity import retry, wait_random_exponential, stop_after_attempt

from src.codevecdb.config.Config import Config


@retry(reraise=True, wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def insert_doc_db(docs_list):
    cfg = Config()
    milvus_uri = cfg.milvus_uri
    user = cfg.milvus_user
    password = cfg.milvus_password
    collection_name = cfg.milvus_collection_name
    embeddings = OpenAIEmbeddings(model="ada")

    vector_store = Milvus(collection_name=collection_name, embedding_function=embeddings,
                          connection_args={"uri": milvus_uri, "user": user, "password": password})\
        .from_documents(
        docs_list,
        embedding=embeddings,
        collection_name=collection_name,
        connection_args={"uri": milvus_uri, "user": user, "password": password}
    )
    return vector_store


@retry(reraise=True, wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def search_db(question):
    cfg = Config()
    milvus_uri = cfg.milvus_uri
    user = cfg.milvus_user
    password = cfg.milvus_password
    collection_name = cfg.milvus_collection_name
    embeddings = OpenAIEmbeddings(model="ada")
    docs = Milvus(collection_name=collection_name, embedding_function=embeddings,
                  connection_args={"uri": milvus_uri, "user": user, "password": password})\
        .similarity_search(query=question, collection_nam=collection_name)
    return docs

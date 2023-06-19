from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Milvus

from src.codevecdb.config.Config import Config


def insert_db(docs_list):
    embeddings = OpenAIEmbeddings(model="ada")
    cfg = Config()
    milvus_uri = cfg.milvus_uri
    user = cfg.milvus_user
    password = cfg.milvus_password
    vector_store = Milvus.from_documents(
        docs_list,
        embedding=embeddings,
        connection_args={"uri": milvus_uri, "user": user, "password": password}
    )
    return vector_store


def search_db(question):
    cfg = Config()
    milvus_uri = cfg.milvus_uri
    user = cfg.milvus_user
    password = cfg.milvus_password
    embeddings = OpenAIEmbeddings(model="ada")
    docs = Milvus(embedding_function=embeddings,
                  connection_args={"uri": milvus_uri, "user": user, "password": password}) \
        .similarity_search(question)
    return docs

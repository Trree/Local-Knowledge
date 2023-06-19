
import os

import openai
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import Document
#from langchain.vectorstores import Chroma
from langchain.vectorstores import Milvus

from src.codevecdb.config.Config import Config

if os.getenv("OPENAI_PROXY"):
    OPENAI_PROXY = os.getenv("OPENAI_PROXY")
    openai.proxy = OPENAI_PROXY


def getAnswer(question):
    cfg = Config()
    milvus_uri = cfg.milvus_uri
    user = cfg.milvus_user
    password = cfg.milvus_password

    embeddings = OpenAIEmbeddings(model="ada")
    docs = Milvus(embedding_function=embeddings,
                  connection_args={"uri": milvus_uri, "user": user, "password": password})\
        .similarity_search(question)

    chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="map_reduce", return_intermediate_steps=True)
    query = "What is Milvus?"
    result = chain({"input_documents": docs, "question": query}, return_only_outputs=True)


    return result


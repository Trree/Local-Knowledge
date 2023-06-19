
import os

import openai
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI
from src.codevecdb.milvus_vectordb import search_db


if os.getenv("OPENAI_PROXY"):
    OPENAI_PROXY = os.getenv("OPENAI_PROXY")
    openai.proxy = OPENAI_PROXY


def getAnswer(question):
    docs = search_db(question)
    chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="map_reduce", return_intermediate_steps=True)
    result = chain({"input_documents": docs, "question": question}, return_only_outputs=True)

    return result


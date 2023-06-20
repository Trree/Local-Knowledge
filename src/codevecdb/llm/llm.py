
import os

import openai
from gptcache.adapter.langchain_models import LangChainLLMs
from langchain import PromptTemplate
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI

from src.codevecdb.db.milvus_vectordb import search_db
from src.codevecdb.llmcache import cache_initialize

if os.getenv("OPENAI_PROXY"):
    OPENAI_PROXY = os.getenv("OPENAI_PROXY")
    openai.proxy = OPENAI_PROXY

cache_initialize()

def getAnswer(question):
    docs = search_db(question)
    if len(docs) == 0:
        return "向量数据库中没有查询到结果"

    my_question_prompt_template = """Use the following portion of a long document to see if any of the text is relevant to answer the question. 
        Return any relevant text verbatim.
        {context}
        Question: {question}
        Relevant text, if any:"""
    MY_QUESTION_PROMPT = PromptTemplate(
        template=my_question_prompt_template, input_variables=["context", "question"]
    )

    #llm = LangChainLLMs(llm=OpenAI(temperature=0))
    llm=OpenAI(temperature=0)
    chain = load_qa_with_sources_chain(llm, chain_type="map_reduce",
                                       return_intermediate_steps=True, question_prompt=MY_QUESTION_PROMPT)
    result = chain({"input_documents": docs, "question": question}, return_only_outputs=True)

    return result["output_text"]


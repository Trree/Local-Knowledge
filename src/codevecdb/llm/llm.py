
import os

import openai
from langchain import PromptTemplate
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI
from src.codevecdb.db.milvus_vectordb import search_db


if os.getenv("OPENAI_PROXY"):
    OPENAI_PROXY = os.getenv("OPENAI_PROXY")
    openai.proxy = OPENAI_PROXY


def getAnswer(question):
    docs = search_db(question)

    my_question_prompt_template = """Use the following portion of a long document to see if any of the text is relevant to answer the question. 
    Return any relevant text verbatim.
    {context}
    Question: {question}
    Relevant text, if any:"""
    MY_QUESTION_PROMPT = PromptTemplate(
        template=my_question_prompt_template, input_variables=["context", "question"]
    )

    chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="map_reduce",
                                       return_intermediate_steps=True, question_prompt=MY_QUESTION_PROMPT)
    result = chain({"input_documents": docs, "question": question}, return_only_outputs=True)

    return result["output_text"]


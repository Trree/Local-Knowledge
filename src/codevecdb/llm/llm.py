
from langchain.llms import OpenAI
from langchain import PromptTemplate
import os
import openai

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from langchain.vectorstores import Milvus

if os.getenv("OPENAI_PROXY"):
    OPENAI_PROXY = os.getenv("OPENAI_PROXY")
    openai.proxy = OPENAI_PROXY


def getAnswer(text_list, question):
    llm = OpenAI()
    documents = []
    for textObj in text_list:
        doc = Document(page_content=textObj["text"], metadata={"source": "database"})
        documents.append(doc)
    
    embeddings = OpenAIEmbeddings()
    
    vectorstore = Chroma.from_documents(documents, embeddings)

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    result = conversation_chain.run(question)
    return result


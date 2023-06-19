
from langchain.llms import OpenAI
from langchain import PromptTemplate
import os
import openai
if os.getenv("OPENAI_PROXY"):
    OPENAI_PROXY = os.getenv("OPENAI_PROXY")
    openai.proxy = OPENAI_PROXY


def getTextSemantics(text):
    llm = OpenAI(temperature=0.3)
    template = """
    You are a text expert who can understand the semantics of text  well. 
    Description of the text's semantics in around 50 words:
    {text}
    Your output needs to be in JSON format and include one fields.
    semantics: text semantics
    """
    prompt = PromptTemplate(
        input_variables=["text"],
        template=template,
    )

    return llm(prompt.format(text=text))


def getAnswer(textList, question):
    llm = OpenAI()
    split_documents = []
    documents = []
    for textObj in textList:
        doc = Document(page_content=textObj["text"], metadata={"source": "database"})
        documents.append(doc)
    text_splitter = CharacterTextSplitter()
    split_documents = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(split_documents, embeddings)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    result =conversation_chain.run(question)
    return result


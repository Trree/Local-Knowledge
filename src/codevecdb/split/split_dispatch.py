import os

from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

from src.codevecdb.config.Config import conf, Config
from src.codevecdb.milvus_vectordb import insert_db


def split_file_to_chunks(file):
    print(file)
    if (not os.path.exists('uploads')):
        os.makedirs('uploads')
    file.save('uploads/' + file.filename)  # 保存文件到指定路径
    loader = TextLoader('uploads/' + file.filename)
    documents = loader.load()
        
    text_splitter = CharacterTextSplitter(chunk_size=conf.chunk_size, chunk_overlap=conf.chunk_overlap)
    docsList = text_splitter.split_documents(documents)

    vector_store = insert_db(docsList)
    print(vector_store)


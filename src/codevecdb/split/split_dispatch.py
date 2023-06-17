import os

from src.codevecdb.parse_code import batchParseTextAndInsert
from src.codevecdb.split.get_language import get_language
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from src.codevecdb.config.Config import conf

def split_file_to_chunks(file):
    print(file)
    if (not os.path.exists('uploads')):
        os.makedirs('uploads')
    file.save('uploads/' + file.filename)  # 保存文件到指定路径
    loader = TextLoader('uploads/' + file.filename)
    documents = loader.load()
        
    text_splitter = CharacterTextSplitter(chunk_size=conf.chunk_size, chunk_overlap=conf.chunk_overlap)
    docsList = text_splitter.split_documents(documents)

    textList = []
    for doc in docsList:
        textList.append(doc.page_content)
    batchParseTextAndInsert(textList)



from src.codevecdb import langchianEmbedding
from src.codevecdb.milvus_vectordb import searchVectorCode, searchRecentData
from src.codevecdb.llm import getAnswer

def searchCode(query, top_k=5):
    semantics_list = [query]
    print(semantics_list)
    codeVectorList = langchianEmbedding.get_semantics_vector(semantics_list)
    dataBaseData = searchVectorCode(codeVectorList, top_k)
    answer = getAnswer(dataBaseData, query)
    return {"answer":answer}


def getAllCode(top_k=100):
    return searchRecentData(top_k)

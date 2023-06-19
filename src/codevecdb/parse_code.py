from src.codevecdb.embeddings.langchainEmbedding import get_semantics_vector
from src.codevecdb.milvus_vectordb import batchInsert


def parseCodeAndInsert(code):
    code_list = [code]
    batchParseTextAndInsert(code_list)
    return 


def batchParseTextAndInsert(text_list):
    if not text_list:
        return ["text_list empty"]
    result_dict= getSemanticsAndVector(text_list, False)
    batchInsert(result_dict)


def getSemanticsAndVector(text_list):
    textVector = get_semantics_vector(text_list)
    result_dict = {}
    for txt, textVector_item in zip(text_list, textVector):
        result_dict[txt] = {"txt": txt, "textVector": textVector_item}
    return result_dict


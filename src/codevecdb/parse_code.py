
from concurrent.futures import ThreadPoolExecutor

from src.codevecdb import llm
from src.codevecdb.langchianEmbedding import get_semantics_vector
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
  


def getSemanticsAndVector(text_list, asyncRequest):
    # if asyncRequest:
    #     with ThreadPoolExecutor() as executor:
    #         futures = [executor.submit(llm.getFunctionSemantics, item.page_content) for item in text_list]
    #         semantics = [future.result() for future in futures]
    # else:
    #     semantics = []
    #     for item in text_list:
    #         semantics.append(llm.getFunctionSemantics(item.page_content))
    
    textVector = get_semantics_vector(text_list)
    result_dict = {}
    for txt, textVector_item in zip(text_list, textVector):
        result_dict[txt] = {"txt": txt, "textVector": textVector_item}
    return result_dict


from concurrent.futures import ThreadPoolExecutor
from itertools import cycle

from langchain.embeddings import OpenAIEmbeddings
from tenacity import retry, wait_random_exponential, stop_after_attempt

from src.codevecdb.config.Config import Config


def split_list(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]


def batchGetEmbedding(test_list):
    cfg = Config()
    key_list = []
    if cfg.openai_key_pool:
        key_list = cfg.openai_key_pool.split(",")
    key_list.append(cfg.openai_api_key)
    unique_key = list(set(key_list))
    embeddings = []
    with ThreadPoolExecutor() as executor:
        all_code_list = split_list(test_list, len(unique_key))
        key_cycle = cycle(unique_key)
        for sub_code_list in all_code_list:
            print("code_list " + str(sub_code_list))
            futures = []
            for item in sub_code_list:
                api_key = next(key_cycle)
                futures.append(executor.submit(getTextEmbedding, item, api_key))
            embeddings.extend([future.result() for future in futures])
    return embeddings


@retry(reraise=True, wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def getTextEmbedding(text, api_key):
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    query_result = embeddings.embed_query(text)
    return query_result

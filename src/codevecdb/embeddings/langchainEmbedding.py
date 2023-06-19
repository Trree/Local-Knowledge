from concurrent.futures import ThreadPoolExecutor

from src.codevecdb.embeddings.bert_vector import semantics_vector
from src.codevecdb.config.Config import Config
from src.codevecdb.embeddings.openai_embeddings import  batchGetEmbedding


def get_semantics_vector(semantics_list):
    cfg = Config()
    if cfg.vector_embeddings == "openai":
        batchGetEmbedding(semantics_list)
    else:
        with ThreadPoolExecutor() as executor:
            print(semantics_list)
            futures = [executor.submit(semantics_vector, item) for item in semantics_list]
            print(futures)
            codeVector = []
            for f in futures:
                codeVector.append(f.result())

    return codeVector

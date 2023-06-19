from concurrent.futures import ThreadPoolExecutor

from src.codevecdb.embeddings.bert_vector import batch_get_vector
from src.codevecdb.config.Config import Config
from src.codevecdb.embeddings.openai_embeddings import  batchGetEmbedding


def get_semantics_vector(semantics_list):
    cfg = Config()
    if cfg.vector_embeddings == "openai":
        text_vector = batchGetEmbedding(semantics_list)
    else:
        text_vector = batch_get_vector(semantics_list)

    return text_vector

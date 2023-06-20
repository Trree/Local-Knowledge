from gptcache import cache
from gptcache.manager import VectorBase, get_data_manager, CacheBase
from gptcache.similarity_evaluation import SearchDistanceEvaluation
from langchain.embeddings import OpenAIEmbeddings

from src.codevecdb.config.Config import Config

embeddings = OpenAIEmbeddings(model="ada")
cache_base = CacheBase('sqlite')

cfg = Config()
connection_args_uri = {
    "uri": cfg.milvus_uri,
    "user": cfg.milvus_user,
    "password": cfg.milvus_password
}

connection_args_host = {
    "host": cfg.milvus_host,
    "port": cfg.milvus_port,
    "user": cfg.milvus_user,
    "password": cfg.milvus_password
}

if cfg.milvus_uri:
    vector_base = VectorBase('milvus', host=cfg.milvus_host, port=cfg.milvus_port, dimension=1596, collection_name='chatbot')
else:
    vector_base = VectorBase('milvus', host='127.0.0.1', port='19530', dimension=1596, collection_name='chatbot')

data_manager = get_data_manager(cache_base, vector_base)

cache.init(
    embedding_func=embeddings,
    data_manager=data_manager,
    similarity_evaluation=SearchDistanceEvaluation())

cache.set_openai_key()

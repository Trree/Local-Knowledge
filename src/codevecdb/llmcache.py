from gptcache import cache
from gptcache.embedding import OpenAI
from gptcache.manager import VectorBase, get_data_manager, CacheBase
from gptcache.similarity_evaluation import SearchDistanceEvaluation
from src.codevecdb.config.Config import Config


def cache_initialize():
    print("start init cache")
    openai = OpenAI()
    cache_base = CacheBase('sqlite')

    cfg = Config()
    print(cfg.milvus_uri + " " + cfg.milvus_user + ":" + cfg.milvus_password)
    if cfg.milvus_uri:
        vector_base = VectorBase('milvus', uri=cfg.milvus_uri,
                                 user=cfg.milvus_user,
                                 password=cfg.milvus_password,
                                 dimension=openai.dimension,
                                 collection_name=cfg.milvus_collection_name)
    else:
        vector_base = VectorBase('milvus',
                                 host=cfg.milvus_host,
                                 port=cfg.milvus_port,
                                 user=cfg.milvus_user,
                                 password=cfg.milvus_password,
                                 dimension=openai.dimension,
                                 collection_name=cfg.milvus_collection_name)

    data_manager = get_data_manager(cache_base, vector_base)

    cache.init(
        embedding_func=openai.to_embeddings,
        data_manager=data_manager,
        similarity_evaluation=SearchDistanceEvaluation())

    cache.set_openai_key()
    print("success init cache")

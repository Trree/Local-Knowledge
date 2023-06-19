from concurrent.futures import ThreadPoolExecutor

from langchain.embeddings import HuggingFaceEmbeddings

from src.codevecdb.config.Config import Config


def batch_get_vector(test_list):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(semantics_vector, item) for item in test_list]
        print(futures)
        codeVector = []
        for f in futures:
            codeVector.append(f.result())


def semantics_vector(code):
    cfg = Config()
    huggingface_model = cfg.vector_embeddings
    embeddings = HuggingFaceEmbeddings(model_name=huggingface_model)
    print("this is my code: " + code)
    return embeddings.embed_query(code)



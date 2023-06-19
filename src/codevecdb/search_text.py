from src.codevecdb.llm.llm import getAnswer


def searchCode(question, top_k=5):
    answer = getAnswer(question)
    result = {"question": question, "answer": answer}
    print(result)
    return result


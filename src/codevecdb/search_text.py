from src.codevecdb.llm.llm import getAnswer


def search_question(question):
    answer = getAnswer(question)
    result = {"question": question, "answer": answer}
    print(result)
    return result


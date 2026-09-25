def judge(question: str, expects: str, answer: str, results) -> bool:
    if not expects:
        return False

    expects = expects.strip().lower()
    answer = answer.strip().lower()
    return expects in answer
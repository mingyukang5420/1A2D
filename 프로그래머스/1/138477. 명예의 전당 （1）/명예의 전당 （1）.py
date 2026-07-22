def solution(k, score):
    answer = []
    honor = []
    for num in score:
        honor.append(num)
        # print(f"honor before sort: {honor}")
        honor.sort(reverse=True)
        if len(honor) < k:
            answer.append(honor[-1])
            continue
        else:
            honor = honor[:k]
            # print(f"honor after sort: {honor}")
            answer.append(honor[-1])
        # print(f"answer: {answer}")
    return answer
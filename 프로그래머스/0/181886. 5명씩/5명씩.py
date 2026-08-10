def solution(names):
    answer = []
    _len = len(names)
    for idx in range(((_len-1)//5)+1):
        answer.append(names[5*idx])
    return answer
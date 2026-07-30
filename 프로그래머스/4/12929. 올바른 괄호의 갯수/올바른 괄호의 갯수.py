def solution(n):
    answer = 0
    answer_list = [0] * (n+1)
    answer_list[0] = 1
    
    # answer_list 만들기
    for idx in range(n+1):
        for j in range(0, idx):
            answer_list[idx] += answer_list[j] * answer_list[idx-j-1]
    
    print(answer_list)
    
    answer = answer_list[n]
    
    return answer
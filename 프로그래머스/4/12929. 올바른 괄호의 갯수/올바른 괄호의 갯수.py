def solution(n):
    answer = 0
    answer_list = [1] * 15
    
    # answer_list 만들기
    for idx in range(2, n+1):
        cnt = 0
        for j in range(idx):
            cnt += answer_list[j] * answer_list[idx-j-1]
        answer_list[idx] = cnt
    
    print(answer_list)
    answer = answer_list[n]
    
    
    return answer
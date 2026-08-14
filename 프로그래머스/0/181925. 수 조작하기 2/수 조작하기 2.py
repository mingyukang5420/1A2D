def solution(numLog):
    answer = ''
    
    key_dict = {1:"w", -1:"s", 10:"d", -10:"a"}
    
    for idx in range(len(numLog) - 1):
        _next = numLog[idx+1]
        _cur = numLog[idx]
        
        answer += key_dict[_next-_cur]
        
    return answer
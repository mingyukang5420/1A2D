def solution(n):
    answer = 0
    
    dividend_arr = [0] * (n + 1)
    
    for dividend in range(1, n + 1):
        for divisor in range(1, n + 1):
            if dividend % divisor == 0:
                
                dividend_arr[dividend] += 1
                
    for dividend in range(1, n + 1):
        if dividend_arr[dividend] >= 3:
            answer +=1 
            
    return answer
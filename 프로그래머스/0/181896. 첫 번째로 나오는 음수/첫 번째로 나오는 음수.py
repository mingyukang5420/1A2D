def solution(num_list):
    for idx, num in enumerate(num_list):
        if num < 0 :
            return idx
    
    else:
        return -1
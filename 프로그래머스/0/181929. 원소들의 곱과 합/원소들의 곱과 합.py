def solution(num_list):
    prod_num = 1
    _sum = 0
    
    for num in num_list:
        prod_num *= num
        _sum += num
        
    # print(f"[DEBUG] num_list:{num_list}")
    return int(prod_num < _sum**2)
        
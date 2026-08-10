def solution(num_list):
    odd = ""
    even = ""
    
    for num in num_list:
        if num & 0b01:
            odd += str(num)
        else:
            even += str(num)
    
    return int(odd) + int(even)
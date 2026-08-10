def solution(a, b):
    is_a_odd = a&0b01
    is_b_odd = b&0b01
    
    if is_a_odd and is_b_odd:
        return a**2 + b**2
    elif is_a_odd or is_b_odd:
        return 2*(a+b)
    else:
        return abs(a-b)

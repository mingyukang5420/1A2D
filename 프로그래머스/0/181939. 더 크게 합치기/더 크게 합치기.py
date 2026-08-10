def operator(a, b):
    str_b = str(b)
    _len = len(str_b)
    return (a*10**(_len))+b

def solution(a, b):
    num1 = operator(a,b)
    num2 = operator(b,a)
    
    return num1 if num1 >= num2 else num2
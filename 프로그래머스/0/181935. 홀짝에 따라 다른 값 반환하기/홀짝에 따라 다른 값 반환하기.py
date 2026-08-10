def solution(n):
    if n & 0b01:
        k = (n+1)//2
        return k**2
    
    else:
        k = n//2
        return 2*k*(k+1)*(2*k+1)//3
    
def solution(arr, n):
    _len = len(arr)
    
    if _len & 0b01: 
        for idx in range(_len//2 + 1):
            arr[2*idx] += n
    else:
        for idx in range(_len//2):
            arr[2*idx+1] += n
        
    return arr
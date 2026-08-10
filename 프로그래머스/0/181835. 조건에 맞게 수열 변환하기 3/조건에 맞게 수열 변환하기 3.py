def solution(arr, k):
    return [num * k for num in arr] if k&0b01 else [num+k for num in arr]
def solution(arr, idx):
    answer = -1
    for _idx in range(idx, len(arr)):
        if arr[_idx]:
            return _idx
    return answer
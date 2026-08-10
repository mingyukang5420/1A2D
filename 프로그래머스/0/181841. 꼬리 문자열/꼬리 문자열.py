def solution(str_list, ex):
    answer = ''.join([_str for _str in str_list if ex not in _str])
    return answer
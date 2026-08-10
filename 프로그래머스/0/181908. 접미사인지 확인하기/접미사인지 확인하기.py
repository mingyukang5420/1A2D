def solution(my_string, is_suffix):
    _len = len(is_suffix)
    
    print(f"[DEBUG] my_string: {my_string}")
    print(f"[DEBUG] is_suffix: {is_suffix}")
    
    
    print(f"[DEBUG] my_string[-_len:]: {my_string[-_len:]}")
    
    if len(my_string) < _len:
        return 0
    
    return int(my_string[-_len:] == is_suffix)
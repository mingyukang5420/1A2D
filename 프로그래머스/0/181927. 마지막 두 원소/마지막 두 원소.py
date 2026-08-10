def solution(num_list):
    _len = len(num_list)
    final = num_list[_len-1]
    former = num_list[_len-2]
    
    addition = final-former if final > former else 2*final
    num_list.append(addition)
    
    return num_list
def solution(my_string, overwrite_string, s):

    splitted = list(my_string)
    _len = len(overwrite_string)
    print(f"[DEBUG] splitted: {splitted}")
    print(f"[DEBUG] _len: {_len}")

    pos = int(s)

    for idx in range(_len):
        print(f"[DEBUG] idx: {idx}")
        splitted[pos + idx] = overwrite_string[idx]

    answer = "".join(splitted)
    return answer
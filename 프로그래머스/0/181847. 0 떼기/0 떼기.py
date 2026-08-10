def solution(n_str):
    for idx in range(len(n_str)):
        if n_str[idx] == "0":
            continue
        else:
            return n_str[idx:]
def solution(n, control):
    cnt = [0,0]
    
    for _str in control:
        if _str == "w":
            cnt[0] += 1
        elif _str == "s":
            cnt[0] -= 1
        elif _str == "d":
            cnt[1] += 1
        elif _str == "a":
            cnt[1] -= 1
        else:
            continue
    
    return n + 1*cnt[0] + 10*cnt[1]
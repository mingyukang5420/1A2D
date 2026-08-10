def solution(myString):
    answer = myString.split("x")
    answer = [s for s in answer if s != ""]
    
    return sorted(answer)
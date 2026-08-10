def solution(todo_list, finished):
    answer = []
    for idx, _bool in enumerate(finished):
        if not _bool:
            answer.append(todo_list[idx])
    return answer
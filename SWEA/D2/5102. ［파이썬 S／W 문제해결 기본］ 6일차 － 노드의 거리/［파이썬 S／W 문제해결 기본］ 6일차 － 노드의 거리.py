from collections import deque


def bfs(sn: int):
    """
    Args:
        sn (int): start_node
    Returns:
        int: the length of the shortest path from start to goal
    """
    # 변수 초기화
    q = deque()
    q.append(sn)
    visited[sn] = 0

    while q:  # bfs 시작
        cn = q.popleft()  # current_node
        
        if cn == G:  # 목적지 도착하면
            break  # 반복 종료

        for nn in range(V+1):  # next_node
            if adj_matrix[cn][nn] == 1 and visited[nn] == -1:  # 연결되어 있고, 미방문 노드만
                visited[nn] = visited[cn] + 1  # 거리를 1 증가시켜서 기록
                q.append(nn)  # 큐에 저장

    else:
        return 0

    return visited[G]  # cn == G 일때 반복 끝남


T = int(input())


for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        row, col = map(int, input().split())
        adj_matrix[row][col] = 1
        adj_matrix[col][row] = 1

    S, G = map(int, input().split())

    visited = [-1 for _ in range(V + 1)]

    result = bfs(S)

    print(f"#{tc} {result}")


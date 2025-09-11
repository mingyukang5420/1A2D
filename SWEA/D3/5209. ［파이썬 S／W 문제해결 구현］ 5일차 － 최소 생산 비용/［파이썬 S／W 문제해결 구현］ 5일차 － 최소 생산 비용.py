def dfs(row, col, table, v, cost):
    global ans

    # 방문행동 - 비용 계산
    cost += table[row][col]

    # 종료 조건 - 조기 종료
    if ans <= cost:
        return

    if row >= N - 1:
        if ans > cost:
            ans = cost
            return

    # 재귀호출
    for nc in range(N):

        if row < N - 1 and v[nc] is False:
            v[nc] = True
            dfs(row + 1, nc, table, v, cost)
            v[nc] = False  # 백트래킹


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 99 * N * N
    visited = [False for _ in range(N)]

    for col in range(N):
        visited[col] = True
        dfs(0, col, arr, visited, 0)
        visited[col] = False

    print(f"#{tc} {ans}")
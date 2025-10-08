import sys

def dfs(n, cnt):
    global ans

    # 종료 조건 - 가지치기
    if ans >= (cnt + (ND + 1 - n) // 2):
        return

    # 종료 조건 - 정답처리
    if n >= ND:
        ans = max(ans, cnt)
        return

    # 방문행동 - 없음

    # 재귀호출
    for cr, cc in ds[n]:
        if not visited[cr - cc]:
            visited[cr - cc] = True  # 방문 예약
            dfs(n + 2, cnt + 1)  # 행에 비숍 놓고 다음탐색
            visited[cr - cc] = False  # 백트래킹

    dfs(n + 2, cnt)  # 현재 행에서 비숍을 놓지 않고 넘어가기


N = int(sys.stdin.readline().strip())
ND = 2 * N - 1  # number of diagonal
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# diagonal_array_sum
# 대각선의 합을 인덱스로 하고 비숍을 놓을 수 있는 위치인 경우
# 해당 (row, col) 튜플을 value로 저장하는 배열
ds = [[] for _ in range(ND)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            ds[i + j].append((i, j))

visited = [False for _ in range(ND)]

ans = 0
dfs(0, 0)  # 0부터 2씩 증가
temp = ans
ans = 0
dfs(1, 0)  # 1부터 2씩 증가
print(ans + temp)

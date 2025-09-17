def dfs(depth, result, pl, mi, mul, div):
    global min_result
    global max_result

    if depth == N:
        min_result = min(result, min_result)
        max_result = max(result, max_result)
        return

    if pl > 0:
        dfs(depth + 1, result + numbers[depth], pl - 1, mi, mul, div)

    if mi > 0:
        dfs(depth + 1, result - numbers[depth], pl, mi - 1, mul, div)

    if mul > 0:
        dfs(depth + 1, result * numbers[depth], pl, mi, mul - 1, div)

    if div > 0:
        dfs(depth + 1, int(result / numbers[depth]), pl, mi, mul, div - 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_result = 1e+9
    max_result = -1e+9

    plus, minus, multiply, divide = operators
    dfs(1, numbers[0], plus, minus, multiply, divide)

    print(f"#{tc} {max_result - min_result}")
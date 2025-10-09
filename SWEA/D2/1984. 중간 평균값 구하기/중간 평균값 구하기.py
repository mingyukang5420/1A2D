T = int(input())
N = 8
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.sort()
    avg = sum(arr[1:-1]) / N
    print(f"#{tc} {avg:.0f}")
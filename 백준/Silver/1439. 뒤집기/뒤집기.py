import sys

# sys.stdin = open("input.txt")

given_text = sys.stdin.readline().rstrip()

left = given_text[:-1]
right = given_text[1:]

calculated = str(bin(int(left, 2) ^ int(right, 2)))

count = 0
for i in range(len(left)):
    count += int(left[i]) ^ int(right[i])

ans = (count + 1) // 2

print(ans)

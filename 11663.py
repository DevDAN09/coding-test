import sys 
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, M = map(int, input().split())
list_dot = sorted(list(map(int, input().split())))

result = []

for _ in range(M):
    a, b = map(int, input().split())
    left_index = bisect_left(list_dot, a)
    right_index = bisect_right(list_dot, b)

    result.append((right_index,left_index))

print("\n".join(map(str, result)))

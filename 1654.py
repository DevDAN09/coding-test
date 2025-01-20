import sys

input = sys.stdin.readline

def binary_search(list_a, start, min_a, M):
    result = 0
    while start <= min_a:
        mid = (start + min_a) // 2
        count = sum([i // mid for i in list_a])

        if count >= M:
            result = mid
            start = mid + 1 
        else:
            min_a = mid -1
    return result
    

N, M = map(int, input().split())

list_a = []

for _ in range(N):
    list_a.append(int(input()))

print(binary_search(list_a, 1, max(list_a), M))


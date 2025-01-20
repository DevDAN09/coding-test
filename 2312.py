import sys

input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    num = int(input())
    i = 2
    tmp = num
    while i * i <= num:
        cnt = 0
        while tmp % i == 0:
            cnt += 1
            tmp //= i
        if cnt:
            result.append(f"{i} {cnt}")
        i += 1
    if tmp > 1:
        result.append(f"{tmp} 1")

sys.stdout.write('\n'.join(result))
        

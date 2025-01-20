import sys 

input = sys.stdin.readline

N = int(input())

def gcd(a, b):
    if b == 0 : return a
    return gcd(b, a%b)

result = []
print_result = []

for _ in range(N):
    nums = list(map(int, input().split()))
    for i in range(1, len(nums)):
        for j in range(i+1, len(nums)):
            result.append(gcd(nums[i], nums[j]))
    
    print_result.append(str(sum(result)))
    result = []

print("\n".join(print_result))
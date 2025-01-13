from itertools import combinations

T = int(input());

list_a = list(map(int, input().split()));
    
def cal(numbers):
    total = sum(numbers)
    square_sum = sum(x * x for x in numbers)
    return (total * total - square_sum) // 2

print(cal(list_a));
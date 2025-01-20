import sys

input = sys.stdin.readline

def push(min_heap, x):
    min_heap.append(x)
    shift_up(min_heap, len(min_heap) - 1)

def shift_up(min_heap, index):
    parent = (index - 1) //2
    
    while index > 0 and min_heap[parent] > min_heap[index]:
        min_heap[parent], min_heap[index] = min_heap[index], min_heap[parent]
        index = parent
        parent = (index - 1) //2

def pop(min_heap):
    if not min_heap:
        return 0
    
    result = min_heap[0]
    min_heap[0] = min_heap[-1]
    min_heap.pop()

    if min_heap:
        shift_down(min_heap, 0)

    return result

def shift_down(min_heap, target):
    size = len(min_heap)

    while True:
        smallest = target 
        left = 2 * target + 1
        right = 2 * target + 2

        if left < size and min_heap[left] < min_heap[smallest]:
            smallest = left
        if right < size and min_heap[right] < min_heap[smallest]:
            smallest = right
        if smallest == target:
            break

        min_heap[target], min_heap[smallest] = min_heap[smallest], min_heap[target]
        target = smallest
        
N = int(input())
input_list = [int(input()) for _ in range(N)]
min_heap = []

for i in input_list:
    if i == 0:
        print(pop(min_heap))
    else:
        push(min_heap,i)
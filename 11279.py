# max heap

import sys 

input = sys.stdin.readline

def push(max_heap, x):
    max_heap.append(x)
    shift_up(max_heap, len(max_heap) - 1)

def shift_up(max_heap, index):
    parent = (index -1) // 2 
    while index > 0 and max_heap[parent] < max_heap[index]:
        max_heap[parent], max_heap[index] = max_heap[index], max_heap[parent]
        index = parent
        parent = (index - 1) // 2

def pop(max_heap):
    if not max_heap:
        return 0
    
    result = max_heap[0]
    max_heap[0] = max_heap[-1]
    max_heap.pop()
    
    if max_heap:
        shift_down(max_heap, 0)
    return result

def shift_down(max_heap, index):
    size = len(max_heap)

    while True:
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < size and max_heap[left] > max_heap[largest]:
            largest = left
        
        if right < size and max_heap[right] > max_heap[largest]:
            largest = right

        if largest == index:
            break

        max_heap[index], max_heap[largest] = max_heap[largest], max_heap[index]
        index = largest


max_heap = []
list_a = []

N = int(input())

for _ in range(N):
    list_a.append(int(input()))

for i in list_a:
    if i == 0:
        print(pop(max_heap))
    else:
        push(max_heap, i)

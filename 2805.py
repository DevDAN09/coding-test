def max_cut_height(n, m, heights):
    left, right = 0, max(heights)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total_cut = sum(max(0, h - mid) for h in heights)

        if total_cut >= m:
            result = mid  
            left = mid + 1
        else:
            right = mid - 1  

    return result


n, m = map(int, input().split())
heights = list(map(int, input().split()))


print(max_cut_height(n, m, heights))
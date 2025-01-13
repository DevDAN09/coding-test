def max_cut_height(n, m, heights):
    left, right = 0, max(heights)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total_cut = sum(max(0, h - mid) for h in heights)

        if total_cut >= m:
            result = mid  # 현재 높이에서 자른 나무의 길이가 M 이상이면, 높이를 높여본다.
            left = mid + 1
        else:
            right = mid - 1  # 자른 나무의 길이가 M 미만이면, 높이를 낮춘다.

    return result

# 입력 처리
n, m = map(int, input().split())
heights = list(map(int, input().split()))

# 결과 출력
print(max_cut_height(n, m, heights))
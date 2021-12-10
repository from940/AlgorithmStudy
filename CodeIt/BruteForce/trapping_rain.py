
def trapping_rain(buildings):
    rain = 0

    for i in range(1, len(buildings)-1) :
        left = max(buildings[:i])
        right = max(buildings[i+1:])
        low = min(left, right)

        if low >= buildings[i]:
            rain += (low-buildings[i])
    return rain


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

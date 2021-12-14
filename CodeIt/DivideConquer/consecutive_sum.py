
def consecutive_sum(start, end):
    if start == end :
        return start
    else :
        return consecutive_sum(start, end//2) + consecutive_sum(end//2+1, end)

def consecutive_sum2(start, end):
    if start == end :
        return start
    #중앙값
    mid = (start+end) // 2
    return consecutive_sum2(start, mid) + consecutive_sum2(mid+1, end)

# test
print(consecutive_sum2(1, 10))
print(consecutive_sum2(1, 100))
print(consecutive_sum2(1, 253))
print(consecutive_sum2(1, 388))
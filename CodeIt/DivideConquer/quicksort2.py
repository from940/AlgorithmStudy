# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    i = start
    b = start
    p = end

    while i < p:
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    swap_elements(my_list, b, p)
    p = b

    return p

# 퀵 정렬
def quicksort(my_list, start=0, end=None):

    if end == None :
        end = len(my_list) - 1

    """base case"""
    if end-start < 1 :
        return

    p = partition(my_list, start, end)

    quicksort(my_list, start, p-1)
    quicksort(my_list, p+1, end)

# 테스트
test_list = [9, 5, 1, 5, 2, 8, 2, 7, 1, 3, 6, 2, 4, 7, 10, 11, 4, 6]
quicksort(test_list) # start, end 파라미터 없이 호출
print(test_list)
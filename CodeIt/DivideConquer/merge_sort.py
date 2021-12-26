
def merge(list1, list2):
    new_list = []

    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    """
    남은 인덱스 부분 처리 생각 못했다.
    """
    if i == len(list1):
        new_list += list2[j:]
    if j == len(list2):
        new_list += list1[i:]

    return new_list

# 합병 정렬
def merge_sort(my_list):
    # 리스트를 반으로 나눈다.
    if len(my_list) < 2 :
        return my_list

    mid = (len(my_list)) //2
    list1 = my_list[:mid]
    list2 = my_list[mid:]

    """
    그림에서도 계속 2개로 나누고 나누고 나누다 마지막에 더한다
    """
    split1 = merge_sort(list1)
    split2 = merge_sort(list2)

    return merge(split1, split2)


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
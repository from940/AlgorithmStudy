
def binary_search(element, some_list):
    start = 0
    last = len(some_list) - 1

    while True :
        index = (start+last)//2
        if index <0 or index >= len(some_list) :
            break
        if some_list[index] == element :
            return index
        elif some_list[index] > element :
            last = index-1
        else :
            start = index+1



print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
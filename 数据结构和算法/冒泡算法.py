#把一个数组从小到大排序

def bubble_sort(list):
    """冒泡算法 时间复杂度: O(N^2)"""
    unsorted = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
        unsorted = unsorted - 1
    return list

list1 = [2, 4, 1, 3, 7]
print (bubble_sort(list1))
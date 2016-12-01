#coding:utf-8
print "排序和顺序统计量"

#堆排序，一棵二叉树，定点是最小值。对于节点i，他的父节点是i/2，左子树是2i，右子树是2i+1，i从0开始

def modify_heap(list, i):
    size = len(list)
    left = 2*i + 1
    right = 2*i + 2

    largest = i
    if left <= size - 1 and list[left] > list[largest]:
        largest = left

    if right <= size - 1 and list[right] > list[largest]:
        largest = right

    if largest != i:
        temp = list[i]
        list[i] = list[largest]
        list[largest] = temp
        modify_heap(list, largest)


# init_list = [4, 1, 10, 14, 16, 9, 3, 2, 8, 7]
# print init_list
# #
# modify_heap(init_list, 1)
# #
# print init_list
# print "16, 14, 10, 8, 7, 9, 3, 2, 4, 1"

def build_heap(list):
    size = len(list)
    for i in xrange(size/2 - 1, -1, -1):
        modify_heap(list, i)


def sort_heap(list):
    build_heap(list)
    size = len(list)
    result = []

    for i in xrange(0, size):
        size = len(list)
        result.append(list[0])

        if size == 1:
            break

        list[0] = list[size - 1]
        del list[size - 1]

        modify_heap(list, 0)
        print "loop", i

    print result

# init_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# sort_heap(init_list)
# print init_list
# build_heap(init_list)
# print init_list

#快速排序

#将数组进行整理，左边都小于某值，右边都大于某值

def quick_sort_part(list, start, end, middle):
    i = start - 1
    value = list[middle]
    for j in xrange(start, end):
        if list[j] < value:
            i += 1
            temp = list[j]
            list[j] = list[i]
            list[i] = temp

    temp = list[i + 1]
    list[i + 1] = value
    list[middle] = temp

    return i + 1

def quick_sort(list, start, end):
    print "quick sort", start, end
    if start < end:
        middle = quick_sort_part(list,start, end, end)
        print "middle", middle
        quick_sort(list, start, middle - 1)
        quick_sort(list, middle+1, end)


# init_list = [2, 8, 7, 1, 3, 5, 6, 4]
# quick_sort(init_list, 0, 7)
# print  init_list

#计数排序，o（n）

def count_sort(list, max):
    size = len(list)
    result = []
    temp = []

    for i in xrange(0, size):
        result.append(0)

    for i in xrange(0, max + 1):
        temp.append(0)

    for item in list:
        temp[item] += 1

    for i in xrange(1, max + 1):
        temp[i] = temp[i-1] + temp[i]

    for i in xrange(size - 1, -1, -1):
        val = list[i]
        index = temp[val] - 1
        print index
        result[index] = val
        temp[val] -= 1

    return result

# init_list = [2, 5, 3, 0, 2, 3, 0, 3]
# result = count_sort(init_list, 5)
# print result


#桶排序
def bucket_sort(list):
    size = len(list)
    temp = []
    for i in xrange(0, size):
        temp.append([])

    for x in list:
        newVal = int(x*size)
        tempList = temp[newVal]

        toInsert = 0
        for i in xrange(0, len(tempList)):
            toInsert = i
            if tempList[i] > x:
                break

        tempList.insert(toInsert, x)

    result = []
    for list in temp:
        for item in list:
            result.append(item)

    print result

init_list = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
bucket_sort(init_list)

#选择算法
def select(list, start, end, i): #找出list里面第i小的元素
    if start is end:
        return list[start]

    r = quick_sort_part(list, start, end, end)
    k = r - start + 1

    if i == k:
        return list[r]
    elif i < k:
        return select(list, start, r - 1, i)
    else:
        return select(list, r + 1, end, i - k)

init_list = [1,2,3,4,5]
print select(init_list, 0, 4, 5)
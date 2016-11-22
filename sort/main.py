import random
import math

init_list = range(1, 10)

print init_list
random.shuffle(init_list)

print init_list


# insert_sort
def insert_sort(myList):
    size = len(myList)
    for i in range(1, size):
        current = myList[i]

        for j in xrange(0, i):
            if current < myList[j]:
                # myList.remove(current)
                del myList[i]
                myList.insert(j, current)
                break

#insert_sort2
def insert_sort2(myList):
    size = len(myList)
    for i in range(1, size):
        current = myList[i]

        # for j in range(0, i):
        #     if current < myList[j]:
        #         for k in range(i, j, -1):
        #             myList[k] = myList[k-1]
        #
        #         myList[j] = current
        #         break
        k = i - 1
        while current < myList[k] and k >= 0:
            myList[k + 1] = myList[k]
            k -= 1

        myList[k + 1] = current

def merge2(list1, list2):
    len1 = len(list1)
    len2 = len(list2)

    list1.append(10000) #用增加卫兵的方法减少复杂性
    list2.append(10000)

    result = []
    index1 = 0
    index2 = 0

    for i in range(0, len1 + len2):
        if(list1[index1] < list2[index2]):
            result.append(list1[index1])
            index1 += 1
        else:
            result.append(list2[index2])
            index2 += 1

    print result

merge2([2,3,4], [1, 5,6,7])






#
# def findMiddle(myList, start, end):
#     a = myList[start]
#     b = myList[end]
#     c = myList[(end + start) / 2]
#
#     new_list = [a, b, c]
#     new_list.sort()
#     middle_value = new_list[1]
#     # middle_value = 28
#
#     while True:
#         while myList[end] > middle_value:
#             end -= 1
#
#         while myList[start] < middle_value:
#             start += 1
#
#         if start >= end:
#             break
#         else:
#             temp = myList[start]
#             myList[start] = myList[end]
#             myList[end] = temp
#
#     return end
#
#
# # init_list = [24, 52, 11, 94, 28, 36, 14, 80]
# middle_value = findMiddle(init_list, 0, len(init_list) - 1)
#
#
# # quick_sort
# def quick_sort(myList, start, end):
#     while start < end:
#         middle_value = findMiddle(myList, start, end)
#         quick_sort(myList, start, middle_value)
#         start = middle_value + 1
#
#
# # quick_sort(init_list, 0, len(init_list) - 1)
# # print "init_list", init_list
# def merge2(list1, list2):
#     pos1 = 0
#     pos2 = 0
#     end1 = len(list1) - 1
#     end2 = len(list2) - 1
#     result = []
#
#     while pos1 <= end1 and pos2 <= end2:
#         if list1[pos1] < list2[pos2]:
#             result.append(list1[pos1])
#             pos1 += 1
#         else:
#             result.append(list2[pos2])
#             pos2 += 1
#
#     if pos1 >= end1:
#         for i in range(pos2, end2 + 1):
#             result.append(list2[i])
#
#     if pos2 >= end2:
#         for i in range(pos1, end1 + 1):
#             result.append(list1[i])
#
#     return result
#
#
# # mqsort
# def mqsort(myList):
#     start = 0
#     end = len(myList) - 1
#
#     if start >= end:
#         return myList
#
#     middle = (end + start - 1) / 2
#
#     sub1 = myList[start:middle + 1]
#     sub2 = myList[middle + 1:end + 1]
#
#     ret1 = mqsort(sub1)
#     ret2 = mqsort(sub2)
#     return merge2(ret1, ret2)
#
#
# result = mqsort(init_list)
#
#
# # print result
#
#
# def ctstor(mylist, max):
#     count = [0] * max
#
#     for i in mylist:
#         count[i] += 1
#
#     for i in range(1, max):
#         count[i] += count[i - 1]
#
#     print count
#
#     temp = [0] * len(mylist)
#     size = len(mylist)
#
#     for i in range(size - 1, -1, -1):
#         print "---------------------------------"
#         val = mylist[i]
#         temp[count[val] - 1] = val
#         count[val] -= 1
#
#     print temp
#
#
# init_list = [0, 4, 1, 3, 1, 2, 4, 1]
#
#
# # ctstor(init_list, 7)
#
# def rxsort(mylist, p, k):
#     src = list(mylist)
#
#     for i in range(0, p):
#         count = [0] * k
#         temp = [0] * len(mylist)
#
#         base = math.pow(k, i)
#
#         for j in src:
#             # print j, base, k
#             index = (int)(j / base) % k
#             count[index] += 1
#
#         for j in range(1, len(count)):
#             count[j] += count[j - 1]
#
#         for j in range(len(src) - 1, -1, -1):
#             val = src[j]
#             index = (int)(val / base) % k
#
#             temp[count[index] - 1] = val
#             count[index] -= 1
#
#         src = list(temp)
#
#     return src
#
#
# init_list = [302, 253, 611, 901, 529, 102]
# ret = rxsort(init_list, 3, 10)
#
# print ret
#
# def bisearch(myList, target):
#     start = 0
#     end = len(myList)
#
#     while start <= end:
#         middle = (end + start)/2
#
#         if target == myList[middle]:
#             return middle
#
#         if target < myList[middle]:
#             end = middle - 1
#         else:
#             start = middle + 1
#
#     return -1
#
# print bisearch(ret, 901)
#
# for i in xrange(0, 10):
#     print "i", i
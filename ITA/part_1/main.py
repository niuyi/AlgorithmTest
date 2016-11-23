#coding:utf-8
print "The maximum-subarray problem"

init_list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

#暴力方法求解
def method_1(list):
    size = len(list)
    max = 0
    start = 0
    end = 0

    for i in xrange(0, size):
        tempSum = 0
        for j in xrange(i, size):
            tempSum += list[j]
            if tempSum > max:
                max = tempSum
                start = i
                end = j

    return (max, start, end)


#递归的方法求解

def find_max_cross(list, start, end, mid):
    left_max = -100000
    right_max = -100000
    start = 0
    end = len(list) - 1

    temp = 0
    for i in xrange(mid, start - 1, -1):
        temp += list[i]
        if temp > left_max:
            left_max = temp
            start = i

    temp = 0
    for i in xrange(mid + 1, end + 1):
        temp += list[i]
        if temp > right_max:
            right_max = temp
            end = i

    return (left_max + right_max, start ,end)

def method_2(list, start ,end):
    if start >= end:
        return (list[start], start, end)

    mid = (end + start)/2

    left_max = method_2(list, start, mid)
    right_max = method_2(list, mid + 1, end)
    middle_max = find_max_cross(list, start, end, mid)
    #
    if left_max[0] > right_max[0] and left_max[0] > middle_max[0]:
        return left_max

    elif right_max[0] > left_max[0] and right_max[0] > middle_max[0]:
        return right_max

    else:
        return middle_max


def method_3(list):
    max = 0
    size = len(list)
    start = 0
    end = size - 1

    tempMax = 0
    for i in xrange(0, size):
        tempMax += list[i]

        if tempMax > max:
            max = tempMax
            end = i
        elif tempMax < 0:
            tempMax = 0
            start = i + 1

    return (max, start, end)



print "m1", method_1(init_list)
print "m2", method_2(init_list, 0, 15)
print "m3", method_3(init_list)


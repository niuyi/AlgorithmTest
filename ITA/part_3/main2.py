#coding:utf-8
import sys
print "动态规划"

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def max(a, b):
    if a > b:
        return a
    return b


def split(n):

    result = []

    if n == 0:
        return result

    for x in xrange(1, n+1):
        temp = [x]
        b = split(n -x)

        if len(b) == 0:
            result.append(temp)
        else:
            for sub in b:
                result.append(temp + sub)

    return result

def cut_rod_1(p, l):
   result = split(l)

   max_value = 0
   max_items = None

   for x in result:

       temp = 0
       for y in x:
           temp += p[y]
       if temp > max_value:
           max_value = temp
           max_items = x

   print max_value
   print max_items

print "暴力方法求解切割问题"
cut_rod_1(p, 8)



def cut_rod(p, n):
    if n == 0:
        return 0

    result = 0
    max_item = None

    for i in xrange(1, n + 1):
        newValue = p[i] + cut_rod(p, n - i)
        if newValue > result:
            result = newValue
            max_item = i


    return result

print "动态分析方法求解切割问题"
print cut_rod(p, 8)
# print cut_rod_1(p, 10)
# print cut_rod(p, 10)

# print "最长子序列问题LCS"
#
# def print_lcs(b, X, i, j):
#     if i <= 0 or j <= 0:
#         return
#
#     if b[i - 1][j - 1] == "e":
#         print_lcs(b, X, i -1, j -1)
#         print "find ", i - 1
#         print X[i - 1]
#
#     elif b[i - 1][j - 1] == "u":
#         print_lcs(b, X, i -1, j)
#     else:
#         print_lcs(b, X, i, j -1)
#
# def lcs_length(X, Y):
#     m = len(X)
#     n = len(Y)
#
#     c = []
#     b = []
#     for i in xrange(0, m + 1):
#         c.append([])
#         for j in xrange(0, n + 1):
#             c[i].append(-1)
#
#     for i in xrange(0, m):
#         b.append([])
#         for j in xrange(0, n):
#             b[i].append("N")
#
#     for i in xrange(0, m + 1):
#         c[i][0] = 0
#
#     for i in xrange(0, n + 1):
#         c[0][i] = 0
#
#     for i in xrange(0, m ):
#         for j in xrange(0, n):
#             i2 = i + 1
#             j2 = j + 1
#             if X[i] == Y[j]:
#                 c[i2][j2] = c[i2 -1][j2 -1] + 1
#                 b[i][j] = "e"
#             elif c[i2 -1][j2] >= c[i2][j2 - 1]:
#                 c[i2][j2] = c[i2 -1][j2]
#                 b[i][j] = "u"
#             else:
#                 c[i2][j2] = c[i2][j2 - 1]
#                 b[i][j] = "l"
#
#
#     for x in c:
#         print x
#
#     # for x in b:
#     #     print x
#     #
#     # print_lcs(b, X, m, n)
#
# # lcs_length(["E", "A", "B", "C", "B", "D", "A", "B"], ["E", "B", "D", "C", "A", "B", "A"])
#
# print "用贪心算法求解活动选择问题"
#
# s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
# f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
#
# def activity_selector(s, f):
#     n = len(s)
#     result = [0]
#     k = 0
#     for i in xrange(1, n):
#         if s[i] >= f[k]:
#             result.append(i)
#             k = i
#
#     print result
#
# activity_selector(s, f)
#
print "0-1背包问题"
v = [60, 100, 120]
w = [10, 20, 30]
#

print "暴力方法求解背包问题"
def find_package_1(v, w, M):
    n = len(v)

    max_value = 0
    result = []


    for i in xrange(0, n):
        temp_value = v[i]
        temp_weight = w[i]
        temp_result = []
        temp_result.append(i)
        for j in xrange(i+1, n):
            if temp_weight + w[j] <= M:
                temp_value += v[j]
                temp_weight += w[j]
                temp_result.append(j)
                if temp_value >= max_value:
                    max_value = temp_value
                    result = temp_result


    print result
    print max_value

def find_package_2(v, w, M, x):
    n = len(v)
    max = 0

    for i in xrange(x, n):
        ret = w[i] + find_package_2(v, w, M-w[i], i + 1)
        if ret <= M:

    # temp_weight = 0
    # temp_value = 0
    #
    # for i in xrange(x, n):
    #     if w[i] + temp_weight <= M:
    #         temp_value = v[i] + find_package_2(v, w, M-w[i], i+1)
    #         temp_weight += w[i]
    #
    # return temp_value

# find_package_1(v, w, 30)
print find_package_2(v, w, 30, 0)




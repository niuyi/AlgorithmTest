def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)


def tailfact(n, a):
    if n == 1:
        return a
    else:
        return tailfact(n-1, a*n)


print "recursive"
print tailfact(10, 1)

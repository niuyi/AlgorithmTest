def get_bit(l, pos):
    mask = 0x80
    temp = pos % 8

    mask >>= temp

    index = pos / 8

    value = l[index]

    if value & mask == mask:
        return 1
    else:
        return 0


def set_bit(l, pos, newValue):
    mask = 0x80
    temp = pos % 8

    mask >>= temp

    index = pos / 8

    value = l[index]

    if newValue == 1:
        l[index] = value | mask
    else:
        l[index] = value & ~mask


def xor_bit(left, right):
    result = []
    size = len(left)

    for i in xrange(0, size):
        result.append(0x00)

    for i in xrange(0, size*8):
        if get_bit(left, i) == get_bit(right, i):
            set_bit(result, i, 0)
        else:
            set_bit(result, i, 1)

    return result


def test(l, pos, value):
    print pos, ":", get_bit(l, pos)
    set_bit(l, pos, value)
    print pos, ":", get_bit(l, pos)


myList = [0xf0, 0x0f]
myList2 = [0x0f, 0xf0]

myList = [0xf0]
myList2 = [0x3c]

print xor_bit(myList, myList2)
# test(myList, 0, 0)
# test(myList, 4, 1)
# test(myList, 10, 1)
# test(myList, 10, 0)
# for i in xrange(0, 16):
#     print get_bit(myList, i)

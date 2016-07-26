def findMath(window, buffer):
    window_len = len(window)
    buffer_len = len(buffer)
    longest = 0
    offset = 0
    next = buffer[0]

    for i in xrange(0, window_len):
        w_pos = i
        b_pos = 0
        length = 0

        while w_pos < window_len and b_pos < buffer_len:
            if window[w_pos] is not buffer[b_pos]:
                break

            w_pos += 1
            b_pos += 1
            length += 1

        if length > longest:
            longest = length
            offset = i
            next = buffer[b_pos]

    return offset, longest, next

print findMath([], ['a', 'b'])

WINDOW_SIZE = 8
BUFFER_SIZE = 4


def compress(src):
    window = []
    buffer = []
    result = []

    for i in xrange(0, WINDOW_SIZE):
        window.append(None)

    for i in xrange(0, BUFFER_SIZE):
        buffer.append(None)

    size = len(src)
    ipos = 0

    for i in xrange(0, BUFFER_SIZE):
        buffer[i] = src[ipos]
        ipos += 1
        if ipos >= size:
            break

    remaining = size

    while remaining > 0:
        find_result = findMath(window, buffer)

        # print "find resutl", find_result

        length = find_result[1]
        if length == 0:
            result.append((0, find_result[2]))
        else:
            result.append((1, find_result))

        remaining -= length + 1
        length += 1

        for i in xrange(0, WINDOW_SIZE - length):
            window[i] = window[i + length]

        temp = 0
        for i in xrange(WINDOW_SIZE - length, WINDOW_SIZE):
            window[i] = buffer[temp]
            temp += 1

        for i in xrange(0, BUFFER_SIZE - length):
            buffer[i] = buffer[i + length]

        for i in xrange(BUFFER_SIZE - length, BUFFER_SIZE):
            if ipos >= size:
                break

            buffer[i] = src[ipos]
            ipos += 1

    return result


src= ['a', 'b', 'a', 'b', 'c', 'b', 'a', 'b', 'a', 'b', 'c', 'a', 'd']

print compress(src)

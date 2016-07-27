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


src = ['a', 'b', 'a', 'b', 'c', 'b', 'a', 'b', 'a', 'b', 'c', 'a', 'd']

compress_result = compress(src)
print "compress_result", compress_result

def uncompress(src):
    result = []
    for i in xrange(0, WINDOW_SIZE):
        result.append(None)

    for item in src:
        if item[0] is 0:
            value = item[1]
            result.append(value)
        else:
            data = item[1]
            offset = data[0]
            length = data[1]
            next = data[2]

            diff = len(result) - WINDOW_SIZE
            posInList = offset + diff

            for i in xrange(0, length):
                result.append(result[posInList])
                posInList += 1

            result.append(next)

    while result[0] is None:
        del result[0]

    return result

print uncompress(compress_result)


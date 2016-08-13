S = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])

A1 = set(['a', 'b', 'c', 'd'])
A2 = set(['e', 'f', 'g', 'h', 'i'])
A3 = set(['j', 'k', 'l'])
A4 = set(['a', 'e'])
A5 = set(['b', 'f', 'g'])
A6 = set(['c', 'd', 'g', 'h', 'k', 'l'])
A7 = set(['l'])

P = [A1, A2, A3, A4, A5, A6, A7]
C = []

sub = S

for p in P:
    C.append(p)
    sub = sub - p
    if len(sub) == 0:
        break

print C





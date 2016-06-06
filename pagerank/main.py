import page
import random

a = page.Page('a')
b = page.Page('b')
c = page.Page('c')
d = page.Page('d')
e = page.Page('e')
f = page.Page('f')
g = page.Page('g')
h = page.Page('h')
i = page.Page('i')
j = page.Page('j')
k = page.Page('k')
l = page.Page('l')
m = page.Page('m')
n = page.Page('n')
o = page.Page('o')
p = page.Page('p')

a.add_pages([e, f, g])
b.add_pages([i, j])
c.add_pages([d])
d.add_pages([k])
e.add_pages([h])
f.add_pages([h, b])
g.add_pages([b, j])
h.add_pages([b])
i.add_pages([j, m])
j.add_pages([n])
k.add_pages([a])
l.add_pages([m])
m.add_pages([j, n, o, p, c])
n.add_pages([d])
o.add_pages([d])
p.add_pages([d])

allList = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
now = allList[0]

for i in range(0, 1000):
    result = random.randint(1, 100)
    if result <= 15:
        random.shuffle(allList)
        now = allList[0]
    else:
        now = now.next_page()

    now.visit()


def mycmp(left, right):
    return left.pv - right.pv

allList.sort(mycmp, reverse=True)
for p in allList:
    print p.name, p.pv


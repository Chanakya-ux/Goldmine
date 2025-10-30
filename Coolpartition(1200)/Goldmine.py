for _ in range(int(input())):
    n = int(input())
    s, l = set(), set()
    c = 0
    for i in input().split():
        s.add(i)
        l.add(i)
        if len(s) == len(l):
            c += 1
            l.clear()
    print(c)
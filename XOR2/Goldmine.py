for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==b:
        print(0)
        continue
    elif b.bit_length()>a.bit_length():
        print(-1)
        continue
    else:
        s = a^b
        if s<=a:
            print(1)
            print(s)
            continue
        else:
            print(2)
            x1 = (1<<(a.bit_length()-1))-1
            x2 = (a^x1)^b
            print(x1,x2)


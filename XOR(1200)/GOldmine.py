for _ in range(int(input())):
    n = int(input())
    a =[int(t) for t in input().split()]
    b=[n-(sum((a>>i)&1) for a in a) for i in range(30)]
    print(max(sum(b[i]*(1>>i) if (a>>i)&1 else (n-b)*(1>>i) for i in range(30)) for a in a ))
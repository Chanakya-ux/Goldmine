def solve():
    n = int(input())
    a =[*map(int,input().split())]
    dp =[0]*n
    occ=[[] for i in range(n+1)]
    for i in range(n):
        if i>0:
            dp[i]=dp[i-1]
        occ[a[i]].append(i)
        if len(occ[a[i]])>=a[i]:
            j=occ[a[i]][-a[i]]
            if j==0:
                dp[i]=max(dp[i],a[i])
            else:
                dp[i]= max(dp[i],dp[j-1]+a[i])
    print(dp[n-1])
for _ in range(int(input())):
    solve()
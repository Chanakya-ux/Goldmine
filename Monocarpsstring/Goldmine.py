def solve():
    n = int(input())
    s = str(input())
    S = s.count('a')-s.count('b')
    lst = {0:-1} # prefix sum - lastindex
    ptr=0;ans=n
    for i in range(n):
        ptr +=1 if s[i]=='a' else -1
        lst[ptr]=i
        if ptr-S in lst:
            ans =min(ans,i-(ptr-S))
    print(-1 if ans ==n else ans)
for _ in range(int(input())):
    solve()
    

from collections import Counter
import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    l, p, r = 0, 1, 1
    
    while l < n:
        if p > n or r > n:
            break
        
        cnt1 = Counter(a[l:p])
        cnt2 = Counter(a[p:r])
        if all(cnt1[x] <= cnt2[x] for x in cnt1):
            ans += 1
            l = p
            p = r
        else:
            r += 1 
            
    print(ans+1)

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

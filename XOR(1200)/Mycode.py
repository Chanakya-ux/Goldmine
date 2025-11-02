import sys
def max_sum(A,n):
    m =[0]*31
    for a in A:
        for j in range(31):
            if (a>>j)&1:
                m[j]+=1
    maxsum=0
    for a in A:
        csum=0
        for j in range(31):
           p=1<<j
           z=n-m[j]
           if (a>>j)&1:
               csum+=z*p
           else:
               csum+=m[j]*p
        maxsum=max(maxsum,csum)
    return maxsum             
        
def solve():
    n=int(input())
    a=[*map(int,input().split())]
    print(max_sum(a,n))
    pass 
def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

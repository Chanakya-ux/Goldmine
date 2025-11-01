def f(x): return 0 if x == 0 else (x-1).bit_length()
def ans(x,y): return f(x) + f(y)
	
purple = []
for _ in range(int(input())):
	n,m,a,b = [int(t) for t in input().split()]
	purple.append( 1+min( ans(n-a+1,m), ans(n,m-b+1), ans(a,m), ans(n,b) ) )
 
print(*purple)
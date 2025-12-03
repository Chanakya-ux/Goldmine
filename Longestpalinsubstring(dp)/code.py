#Given a string s, return the longest palindromic substring in s.
def solve(s):
    n = len(s)
    dp =[[False]*n for _ in range(n)];ans=[0,0]
    for i in range(n):
        dp[i][i]=True
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=True
            ans = (i,i+1)
    for diff in range(2,n):
        for i in range(n-diff):
            j = diff + i
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j]=True
                ans =(i,j)
    i,j = ans
    print(s[i:j+1])
if __name__ == "__main__":
    s ="oprrpoas"
    solve(s)


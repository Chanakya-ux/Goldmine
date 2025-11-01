import sys

def solve():
    n, m, a, b = map(int, input().split())
    gx, gy = m, n
    px, py = b, a
    ans = 0
    M = max(abs(gx - px), abs(px - 1), abs(gy - py), abs(py - 1))
    
    while not (gx == 1 and gy == 1):
        d1=max(abs(gx - px), abs(px - 1));d2=max(abs(gy - py), abs(py - 1))
        d = max(d1,d2)
        if d1==d2:
            cx, cy = (d, 0) if gx>gy else (0,d)
        else:cx, cy = (d, 0) if d in (abs(gx - px), abs(px - 1)) else (0, d)
        gx -= cx
        gy -= cy
        if gx == 1 and gy == 1:
            break
        ans += 1
        px, py = (gx + 1)//2, (gy + 1)//2
    
    ans += 1
    print(ans)
for _ in range(int(input())):
    solve()

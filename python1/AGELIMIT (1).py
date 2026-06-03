t = int(input())

for _ in range(t):
    x, y, a = map(int, input().split())
    
    if x <= a and a < y:
        print("YES")
    else:
        print("NO")
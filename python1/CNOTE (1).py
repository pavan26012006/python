# cook your dish here
t = int(input())

for _ in range(t):
    x, y, k, n = map(int, input().split())
    
    required = x - y
    possible = False
    
    for _ in range(n):
        p, c = map(int, input().split())
        
        if p >= required and c <= k:
            possible = True
    
    if possible:
        print("LuckyChef")
    else:
        print("UnluckyChef")
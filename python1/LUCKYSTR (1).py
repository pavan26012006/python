# cook your dish here
k, n = map(int, input().split())

favorites = [input().strip() for _ in range(k)]

for _ in range(n):
    s = input().strip()
    
    if len(s) >= 47:
        print("Good")
        continue
    
    good = False
    for fav in favorites:
        if fav in s:
            good = True
            break
    
    if good:
        print("Good")
    else:
        print("Bad")
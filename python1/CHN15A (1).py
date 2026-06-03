# cook your dish here
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    count = 0
    for a in arr:
        if (a + k) % 7 == 0:
            count += 1
    
    print(count)
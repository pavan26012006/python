# cook your dish here
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    alice = list(map(int, input().split()))
    berta = set(map(int, input().split()))
    
    count = 0
    
    for x in alice:
        if x in berta:
            count += 1
    
    print(count)
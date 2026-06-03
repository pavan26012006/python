# cook your dish here
# Ciel and Receipt

T = int(input())

for _ in range(T):
    p = int(input())
    
    count = 0
    
    # Use largest menu prices first
    for price in [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]:
        count += p // price
        p = p % price
    
    print(count)
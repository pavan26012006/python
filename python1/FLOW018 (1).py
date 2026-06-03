# cook your dish here
# Small Factorial

T = int(input())

for i in range(T):
    N = int(input())
    
    fact = 1
    
    for j in range(1, N + 1):
        fact = fact * j
    
    print(fact)
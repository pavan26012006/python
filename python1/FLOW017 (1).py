# cook your dish here
# Second Largest

T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    
    numbers = [A, B, C]
    numbers.sort()
    
    # Second largest number
    print(numbers[1])
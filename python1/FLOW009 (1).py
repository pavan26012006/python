# cook your dish here
# Total Expenses

T = int(input())

for _ in range(T):
    quantity, price = map(int, input().split())
    
    total = quantity * price
    
    # Apply 10% discount if quantity > 1000
    if quantity > 1000:
        total = total - (0.10 * total)
    
    print(f"{total:.6f}")
# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))

    best_index = 0
    best_product = L[0] * R[0]
    best_rating = R[0]

    for i in range(1, n):
        product = L[i] * R[i]

        if product > best_product:
            best_product = product
            best_rating = R[i]
            best_index = i
        elif product == best_product:
            if R[i] > best_rating:
                best_rating = R[i]
                best_index = i

    print(best_index + 1)  # 1-based indexing
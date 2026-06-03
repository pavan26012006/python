# cook your dish here
T = int(input())

for _ in range(T):
    N = int(input())

    digit_sum = 0

    while N > 0:
        digit_sum += N % 10
        N //= 10

    print(digit_sum)
# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))

    m = min(w)
    moves = 0

    for salary in w:
        moves += salary - m

    print(moves)
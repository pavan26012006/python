# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if arr != arr[::-1]:
        print("no")
        continue

    expected = 1

    for x in arr:
        if x == expected:
            continue
        elif x == expected + 1:
            expected += 1
        elif x > expected + 1:
            break

    if expected == 7 and all(1 <= x <= 7 for x in arr):
        print("yes")
    else:
        print("no")
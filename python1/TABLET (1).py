# cook your dish here
t = int(input())

for _ in range(t):
    n, b = map(int, input().split())

    max_area = 0

    for _ in range(n):
        w, h, p = map(int, input().split())

        if p <= b:
            area = w * h
            if area > max_area:
                max_area = area

    if max_area == 0:
        print("no tablet")
    else:
        print(max_area)
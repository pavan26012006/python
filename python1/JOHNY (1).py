# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    song = a[k - 1]      # Uncle Johny's song length

    a.sort()

    print(a.index(song) + 1)
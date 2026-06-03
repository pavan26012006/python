# cook your dish here
import math

t = int(input())

for _ in range(t):
    B, LS = map(int, input().split())

    rs_min = math.sqrt(LS * LS - B * B)
    rs_max = math.sqrt(LS * LS + B * B)

    print(f"{rs_min:.5f} {rs_max:.5f}")
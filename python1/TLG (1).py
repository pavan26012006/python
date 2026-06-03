# cook your dish here
n = int(input())

p1 = 0
p2 = 0

max_lead = 0
winner = 0

for _ in range(n):
    s, t = map(int, input().split())
    
    p1 += s
    p2 += t
    
    if p1 > p2:
        lead = p1 - p2
        if lead > max_lead:
            max_lead = lead
            winner = 1
    else:
        lead = p2 - p1
        if lead > max_lead:
            max_lead = lead
            winner = 2

print(winner, max_lead)
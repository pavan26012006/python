# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

import sys

data = sys.stdin.read().split()

N = int(data[0])
K = int(data[1])

count = 0

for i in range(2, N + 2):
    if int(data[i]) % K == 0:
        count += 1

print(count)

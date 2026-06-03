a, b = map(int, input().split())

correct = a + b
wrong = a * b

print(abs(correct - wrong))
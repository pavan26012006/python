n, a, b = map(int, input().split())

# users who made at least one submission
rated_users = n - a

# users who solved at least one problem (rating > 1000)
high_rated = rated_users - b

print(rated_users, high_rated)
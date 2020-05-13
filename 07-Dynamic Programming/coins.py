import math

coins = [1, 3, 4]


# recursive solution to minimum number of coins problem


def c_solve(x):
    if x < 0:
        return math.inf
    elif x == 0:
        return 0
    best = math.inf
    for c in coins:
        best = min(best, c_solve(x - c) + 1)
    return best


print(c_solve(10))  # solves quickly
print(c_solve(30))  # takes several seconds
# print(c_solve(100)) #times out

# ======================================================================
# optimized recursive solution using dynamic programming and memoization
value = {}


def dp_solve(x):
    if x < 0:
        return math.inf
    elif x == 0:
        return 0
    try:
        return value[x]
    except:
        pass
    best = math.inf
    for c in coins:
        best = min(best, dp_solve(x - c) + 1)
    value[x] = best
    return best


print(dp_solve(30))  # solves quickly
print(dp_solve(100))  # solves quickly

# ========================================================================
# iterative version of dynamic programming solution, with solution printed
value = {0: 0}
first = {}


def it_solve(n):
    for x in range(1, n + 1):
        value[x] = math.inf
        for c in coins:
            if x - c >= 0 and value[x - c] + 1 < value[x]:
                value[x] = value[x - c] + 1
                first[x] = c
    return value[n], first[n]


n = 33
it_solve(n)
while n > 0:
    print(first[n])
    n -= first[n]

# ===========================================
# total number of solutions for each coin sum
count = [1]
n = 33
for x in range(n + 1):
    count.append(0)
    for c in coins:
        if x - c >= 0:
            count[x] += count[x - c]
print(count[33])

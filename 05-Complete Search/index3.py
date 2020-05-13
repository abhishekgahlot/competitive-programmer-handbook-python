# recursive subset generation, gives all combinations of a set (not permutations)
n = 5
subset = []
combinations = []


def search(k):
    if k == n:
        # process subset
        combinations.append(subset.copy())
    else:
        search(k + 1)
        subset.append(k)
        search(k + 1)
        subset.pop()


search(0)
print(combinations)

# ===========================================================
# recursive permutation generation, always selects n elements
n = 3
perm = []
permutations = []
chosen = [0] * n


def p_search():
    if len(perm) == n:
        # process permutation
        permutations.append(perm.copy())
    else:
        for i in range(n):
            if chosen[i]: continue
            chosen[i] = 1
            perm.append(i)
            p_search()
            chosen[i] = 0
            perm.pop()


p_search()
print(permutations)

# ===========================================================
# backtrack solution to solving n queens on an nxn chessboard
n = 4
count = [0]
column = [0 for _ in range(n)]
diag1 = [0 for _ in range(2 * n - 1)]
diag2 = [0 for _ in range(2 * n - 1)]


def q_search(y):
    if y == n:
        count[0] += 1
        return
    for x in range(n):
        if column[x] or diag1[x + y] or diag2[x - y + n - 1]: continue
        column[x] = diag1[x + y] = diag2[x - y + n - 1] = 1
        q_search(y + 1)
        column[x] = diag1[x + y] = diag2[x - y + n - 1] = 0


q_search(0)
print(count[0])

# ===========================================================


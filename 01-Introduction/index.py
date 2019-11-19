# Input -> 10 20 monkey
a, b, c = raw_input().split(' ')
print(a, b, c)

# Input with map -> 10 20
a, b = map(int, raw_input().split(' '))
print(a, b)

# Input with map -> 10, 20
a, b = map(int, raw_input().split(','))
print(a, b)
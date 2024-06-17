


def fib(n, memo=None):
    if memo is None: memo = {} # Assign a default dict if noe is passed
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


my_dict = {1: 'one', 2: 'two', 3: 'three'}

"""
print(fib(7))
print(fib(20))
print(fib(50))
print(fib(7))
"""

# Grid Traveller
def gridTraveler(m, n, memo=None):
    key = "{},{}".format(m, n)
    if memo is None:    memo = {}
    if key in memo: return memo[key]

    if m == 1 and n == 1:   return 1
    if m == 0 or n == 0:    return 0
    
    memo[key] = gridTraveler(m -1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[key]


print(gridTraveler(1, 1)) # 1
print(gridTraveler(2, 3)) # 3
print(gridTraveler(3, 2)) # 3
print(gridTraveler(3, 3)) # 6
print(gridTraveler(18, 18))






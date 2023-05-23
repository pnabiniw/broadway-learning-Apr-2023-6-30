# Without recursion
fact = 1
for i in range(1, 6):
    fact *= i

print(fact)


# With recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(5))

# 5 * factorial(4)  => 5 * 24 = 120
# 4 * factorial(3) => 4 * 6 = 24
# 3 * factorial(2)  => 3 * 2 = 6
# 2 * factorial(1)  => 2 * 1 = 2
# 1 * factorial(0) => 1 * 1 = 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

probability_success = 1.09/2.09
probability_failure = 1 - (1.09/2.09)
n = 6 #Number of children
r = 3  #Number of boys
answer = 0


def factorial(n):
    f = 1
    for i in range(n):
        temp = n - i
        f *= temp
    return f

def combination(n,r):
    num = 1
    denom = 1
    num = factorial(n)
    denom = factorial(r) * factorial(n-r)
    combo = num/denom
    return combo

for iteration in range(n):
    if r > n:
        break
    combo = combination(n,r)
    success = pow(probability_success, r)
    failure = pow(probability_failure, n-r)
    answer += ((combo*success*failure))
    r += 1
print(round(answer,3))

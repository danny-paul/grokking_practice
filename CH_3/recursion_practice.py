# Returns the factorial, !n, of the passed parameter, n. Postiive integers only. Solution by recursion
# Eg: !5--> 5 * 4 * 3 * 2 * 1
def factorial_by_recursion(n: int):
    if (n > 1):
        return n * factorial_by_recursion(n - 1)
    else:
        return 1
    
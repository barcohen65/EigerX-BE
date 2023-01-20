def recursive_sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + recursive_sum_of_digits(n // 10)
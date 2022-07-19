def fibonacci(n):
    """
    Returns number at index n of the fibonacci sequence.
    :param n:
    :return:
    """
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

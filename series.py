def fibonacci(n):
    """
    Returns number at index n of the fibonacci sequence.
    :param n:
    :return fibonacci(n-1) + fibonacci(n-2):
    """
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
    Returns number at index n of the lucas sequence.
    :param n:
    :return lucas(n-1) + lucas(n-2):
    """
    if n <= 0:
        return 2
    if n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)

def sum_series(n, int1=0, int2=1):
    """
    Returns number at index n of either lucas or fibonacci sequence
    :param n:
    :param int1:
    :param int2:
    :return return fibonacci(n) or lucas(n):
    """
    if int1 == 0 and int2 == 1:
        return fibonacci(n)
    if int1 == 2 and int2 == 1:
        return lucas(n)
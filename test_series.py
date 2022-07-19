from series import fibonacci

def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fibonacci_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_six():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_fibonacci_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

def test_fibonacci_eight():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected
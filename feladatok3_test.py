from feladatok3 import sum_numbers

def test_sum_numbers():
    result = sum_numbers(2, 3)
    assert 5 == result

def test_sum_numbers_zero():
    result = sum_numbers(0, 0)
    assert 0 == result


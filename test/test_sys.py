import sys


def test_get_ref_count():
    numbers = [1, 2, 3]
    ref_count = 1
    assert ref_count + 1 == sys.getrefcount(numbers)

    # more_numbers = numbers
    ref_count += 1
    assert ref_count + 1 == sys.getrefcount(numbers)

    # total = sum(numbers)
    assert ref_count + 1 == sys.getrefcount(numbers)

    # matrix = [numbers, numbers, numbers]
    ref_count += 3
    assert ref_count + 1 == sys.getrefcount(numbers)
    assert 6 == sys.getrefcount(numbers)


def test_platform():
    assert "win32" == sys.platform

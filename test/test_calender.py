import calendar
import datetime


def test_1():
    assert 0 == calendar.MONDAY
    assert (calendar.MONDAY, 31) == calendar.monthrange(2023, 5)
    assert (calendar.THURSDAY, 30) == calendar.monthrange(2023, 6)


def test_2():
    assert 31 == calendar.mdays[1]
    for d in range(1, calendar.mdays[datetime.datetime.now().month] + 1):
        print(d)

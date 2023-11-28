import datetime
import time


def test_compare():
    print("\n------------------")
    d1 = datetime.date(2022, 10, 30)
    d2 = datetime.datetime.now().date()
    d_delta = d2 - d1
    print(d_delta)


def test_string_format():
    d1 = datetime.date(2022, 10, 30)
    print(d1.strftime("%m- hwdhwd%d/%Y, %M:%S"))  # 01/14/2023, 13:09:07
    dt2 = datetime.datetime.strptime("06- hwdhwd07/2023, 35:51", "%m- hwdhwd%d/%Y, %M:%S")
    print(dt2)
    assert "October 30, 2022" == f"{d1:%B %d, %Y}"


def test_diff():
    d1 = datetime.datetime.now()
    time.sleep(0.7)
    d2 = datetime.datetime.now()
    d_delta = d2 - d1
    print(d_delta)
    print(f"days :{d_delta.days} microseconds :{d_delta.microseconds}")


def test_date_delta():
    d1 = datetime.date(2022, 10, 30)
    d2 = d1 + datetime.timedelta(days=-5)
    assert d2.month == 10
    assert d2.day == 25
    d3 = d1.replace(month=3)
    assert d1.month == 10

    assert d3.month == 3
    assert d3.day == 30
from src.person import Person

# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting


def test_str1():
    assert "0000005" == f"{5:07}"
    assert "0000010" == f"{10:07}"
    assert "0x000000a" == f"0x{10:07x}"
    assert "1,234,567.99" == f"{1234567.9876:,.2f}"  # Comma as thousand separators and two decimals:
    assert "-1_234_567" == f"{-1234567:{'_'}}"
    assert "======-1234567======" == f"{'-1234567':=^20}"


def test_sub_str():
    s: str = "01234567890"
    assert "01234" == s[0:5]


def test_1():
    key = "q"
    value = ["1", "2"]
    assert "q  2    " == f"{key:<3}{value[1]:<5}"


def test_compare():
    str1 = "scs PoC : fx0233 f"
    str2 = "poc :"
    assert str2.casefold() in str1.casefold()


def test_hex():
    a = 255
    assert "0xff" == hex(a)
    assert "FF" == f"{a:X}"

    assert "ff" == f"{a:x}"
    assert " ff" == f"{a:3x}"
    assert "0ff" == f"{a:03x}"
    assert "0FF" == f"{a:03X}"

    assert "0xff" == f'{a:#x}'
    assert "0XFF" == f'{a:#X}'
    assert "0b11111111" == f'{a:#b}'
    assert "ff" == f"{a:x}"


def test_person():
    jane = Person("Jane Doe", 25)
    assert "I'm Jane Doe, and I'm 25 years old." == f"{jane}"
    assert "I'm Jane Doe, and I'm 25 years old." == f"{jane!s}"
    assert "Person(name='Jane Doe', age=25)" == f"{jane!r}"
    print(jane)


def test_var():
    variable = "Some mysterious value"
    assert "variable = 'Some mysterious value'" == f"{variable = }"


def test_zfill():
    assert "00042" == "42".zfill(5)
    assert "-0042" == "-42".zfill(5)
    assert "00abc" == "abc".zfill(5)
    assert "+0abc" == "+abc".zfill(5)


def test_list():
    # new_list = [expression for item in iterable if condition == True]
    input_list = ["a", "b", "c"]
    bs = "\n"
    assert """list:
a
b
c""" == f"list:\n{bs.join(a for a in input_list)}"

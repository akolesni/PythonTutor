def test_str1():
    assert "0000005" == f"{5:07}"
    assert "0000010" == f"{10:07}"
    assert "0x000000a" == f"0x{10:07x}"


def test_sub_str():
    s: str = "01234567890"
    assert "01234" == s[0:5]


def test_1():
    key = "q"
    value = ["1", "2"]
    assert "q  2    " == f"{key:<3}{value[1]:<5}"


def test_cmpare():
    str1 = "scs PoC : fx0233 f"
    str2 = "poc :"
    assert str2.casefold() in str1.casefold()

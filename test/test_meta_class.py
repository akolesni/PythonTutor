#  https://habr.com/ru/companies/otus/articles/527384/
class LittleMeta(type):
    def __new__(metacls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(metacls, clsname, superclasses, attributedict)


class S:
    pass


class A(S, metaclass=LittleMeta):
    pass


def test_1():
    print("\nTEST")
    print(A())

class A(object):
    _a = 'AAA'
    _A = "AAAAAAAA"
    __a = 'LLLLL'

    def __hello(self):
        print("hello")

class B(A):
    pass


if __name__ == "__main__":
    a = A()
    b = B()

    print(dir(a))
    print(a._a)
    print(a._A__a)
    print(a._A__hello())
    # print(b._A)
    print(dir(b))
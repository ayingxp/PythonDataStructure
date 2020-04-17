class A(object):
    def __hello__(self):
        print("hello method from A class")

    def __func(self):
        print("A method")


class B(A):
    pass


# a = range(10)
# print(a)
# print(type(a))
# for i in a:
#     print(i, end=" ")
#
# for i in a:
#     print(i, end=" ")
# exit(0)

if __name__ == "__main__":
    a = A()
    a.__hello__()
    b = B()
    print(dir(b))
    b.__hello__()
    b._A__func()
    smaller = input("enter the num: ")
    big = input("enter big: ")
    print(smaller)
    print(big)
    print(type(big))

    a = 1
    b = 2
    a, b = b, a
    print(a)
    print(b)


def test_function(*args):
    """test function"""
    for a in args:
        print(a)
    print(type(args))


test_function("a", "b", "c")


def test_function2(**kwargs):
    """test function"""
    for k, v in kwargs.items():
        print(f"{k}:{v}")
    print(type(kwargs))


test_function2(a="A", b="B", c="C")

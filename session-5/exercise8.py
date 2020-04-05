from contextlib import contextmanager


@contextmanager
def do_something(a):
    print(f"a is {a}")
    print('start')
    yield a
    print("end")


def main():
    with do_something("3") as x:
        print(x)


if __name__ == '__main__':
    main()

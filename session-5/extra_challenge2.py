from time import sleep
from functools import wraps


def delay(seconds, repeat=1):
    def inner_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(repeat):
                print(f"START {func.__name__}")
                print(_)
                sleep(seconds)
                output = func(*args, **kwargs)
                print(f"END {func.__name__}")
            return output
        return wrapper
    return inner_function


@delay(seconds=5, repeat=2)
def main(word):
    print(word)


if __name__ == '__main__':
    main("haha")

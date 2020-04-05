from functools import wraps
from IPython import embed


def debug_input_and_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"ARGS {args}")
        print(f"KWARGS {kwargs}")
        output = func(*args, **kwargs)
        print(f"OUTPUT {output}")
        return output
    return wrapper


@debug_input_and_output
def say_something(word):
    print(word)


def main():
    say_something("Hi Ryan")


if __name__ == '__main__':
    main()

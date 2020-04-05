from time import sleep
import random


def iterate_delay(repeat):
    for _ in range(repeat):
        print(_)
        delay = random.randint(1, 5)
        print(f"sleeping for {delay} second(s)")
        sleep(delay)


def main():
    iterate_delay(repeat=5)


if __name__ == '__main__':
    main()

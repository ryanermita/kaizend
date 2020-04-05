from time import sleep


def iterate_delay(loop_number, seconds):
    for _ in range(loop_number):
        print(_)
        print(f"sleeping for {seconds} second(s)")
        sleep(seconds)


def main():
    iterate_delay(loop_number=5, seconds=2)


if __name__ == '__main__':
    main()

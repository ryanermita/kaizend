class ScrapingJob:
    def __init__(self, name):
        self.name = name
        self.url = "<none>"
        self.selector = "<none>"
        self.save_file = "<none>"

    def load(self, url):
        self.url = url

        return self

    def find(self, selector):
        self.selector = selector

        return self

    def save(self, save_file):
        self.save_file = save_file

        return self

    def complete(self):
        print(f"[START {self.name}")
        print(f"[URL {self.url}")
        print(f"[SELECTOR {self.selector}")
        print(f"[SAVE FILE {self.save_file}")
        print(f"[END {self.name}")


def main():
    job1 = ScrapingJob("job 1")
    job1.load("<url>").find("<selector").save("<filename>").complete()

    job2 = ScrapingJob("job 2")
    job2.load("<url>").find("<selector").complete()

    job3 = ScrapingJob("job 3")
    job3.load("<url>").complete()


if __name__ == '__main__':
    main()

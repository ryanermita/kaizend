from contextlib import contextmanager


class Job:
    def __init__(self, label):
        self.label = label
        self.target_url = None
        self.selector = None
        self.save_file = None

    def do_something(self):
        print(f"[START {self.label}]")
        print(f"[URL {self.target_url}")
        print(f"[SELECTOR {self.selector}")
        print(f"[SAVE FILE {self.save_file}")
        print(f"[END {self.label}]")


@contextmanager
def scraping_job(label):
    job = Job(label)
    yield job


def main():
    with scraping_job("Job 1") as job:
        job.target_url = "<url2>"
        job.selector = "<selector>"
        job.save_file = "<filename>"
        job.do_something()

    with scraping_job("Job 2") as job:
        job.target_url = "<url 2>"
        job.selector = "<selector 2>"
        job.save_file = "<filename 2>"
        job.do_something()


if __name__ == '__main__':
    main()


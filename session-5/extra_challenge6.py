import requests
from IPython import embed
from time import sleep
import random
from bs4 import BeautifulSoup
from functools import wraps


BASE_URL = 'http://sample-target-bucket-with-html-pages.s3-website-ap-southeast-1.amazonaws.com'
PAGES = [
    'group1/1.html',
    'group1/2.html',
    'group1/3.html',
    'group1/4.html',
    'group1/5.html',
    ]


def debug_input_and_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[START: {func.__name__}]")
        output = func(*args, **kwargs)
        print(f"[END: {func.__name__}]]")
        return output
    return wrapper

@debug_input_and_output
def delay(seconds):
    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)
    return ""


def get_random_number():
    return random.randint(1, 5)


@debug_input_and_output
def extract_html_content(target_url):
    print(f"Downloading HTML content of {target_url}")
    response = requests.get(target_url)
    return response.text


@debug_input_and_output
def extract_target_value_from_page(html_string):
    content = BeautifulSoup(html_string, 'html.parser')
    target = content.find(id='target')
    return target.get_text()


def main():
    for page in PAGES:
        html_url = f"{BASE_URL}/{page}"
        html_content = extract_html_content(html_url)
        print(html_content)
        extract_target_value_from_page(html_content)
        delay(get_random_number())


if __name__ == '__main__':
    main()

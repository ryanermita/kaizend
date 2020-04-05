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


def delay(seconds):
    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)


def get_random_number():
    return random.randint(1, 5)


def extract_html_content(target_url):
    response = requests.get(target_url)
    return response.text


def extract_target_value_from_page(html_string):
    content = BeautifulSoup(html_string, 'html.parser')
    target = content.find(id='target')
    print(target.get_text())
    return target.get_text()


def main():
    for page in PAGES:
        html_url = f"{BASE_URL}/{page}"
        html_content = extract_html_content(html_url)
        extract_target_value_from_page(html_content)
        delay(get_random_number())


if __name__ == '__main__':
    main()

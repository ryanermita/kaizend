import requests
from IPython import embed
from time import sleep
import random
from bs4 import BeautifulSoup
from functools import wraps

BASE_URL = 'https://sample-target-bucket-with-html-pages.s3-ap-southeast-1.amazonaws.com/group3/target.html'


def extract_html_content(target_url):
    response = requests.get(target_url)
    return response.text


def extract_target_value_from_page(html_string):
    content = BeautifulSoup(html_string, 'html.parser')
    li_elements = content.find_all('li')
    for li_element in li_elements:
        li_element_list = li_element.get_text(strip=True).split(' ')
        cleaned = ' '.join(x.strip() for x in li_element_list if x.strip())
        print(cleaned)
        print("")


def main():
    print(f"Downloading HTML content of {BASE_URL}")
    html_content = extract_html_content(BASE_URL)
    extract_target_value_from_page(html_content)


if __name__ == '__main__':
    main()

from bs4 import BeautifulSoup
from IPython import embed
import re


def generate_html():
    return """
        <html>
            <head></head>
            <body>
                <a href="/a.html">A</a>
                <a href="/b.html">B</a>
                <a href="/c.html">C</a>
                <a href="/d.html">D</a>

                <script>
                    var hello = "yoh";
                    alert(hello);
                </script>
            </body>
        </html>
    """


def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html.parser')
    script = soup.find('script')
    pattern = re.compile("var hello = \"(.*?)\";")
    print(pattern.findall(script.text)[0])


if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup

urls = [
    f"https://home.cnblogs.com/blog/page/{page}/"
    for page in range(1, 51)
]


# print(urls)


def craw(url):
    r = requests.get(url)
    # print(url,len(r.text))
    return r.text


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="title_author")
    return [(link["href"], link.get_text()) for link in links]


if __name__ == "__main__":
    # craw(urls[0])
    for result in parse(craw(urls[2])):
        print(result)

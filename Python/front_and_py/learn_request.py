import requests


def requests_jd(keyword):
    url = "https://search.jd.com/Search"
    params = {
        "keyword": keyword
    }
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
    }
    response = requests.get(url=url, params=params, headers=headers)
    print(response.text)


if __name__ == "__main__":
    requests_jd("鼠标")

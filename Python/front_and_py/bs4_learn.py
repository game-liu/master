from bs4 import BeautifulSoup


def jd_search_parse(html):
    # 去除空格、换行等
    html = html.replace('\r\n', '').replace('\n', '').replace('\t', '')
    soup = BeautifulSoup(html, 'lxml')
    item = soup.select("li[data-sku='10031287137870']")[0]
    # print(item.text)
    print(item.next_sibling.next_sibling)  # 获取下一个节点
    # print(item.text)


if __name__ == "__main__":
    with open('jd_search.html', 'r', encoding='utf-8') as f:
        html = f.read()
    jd_search_parse(html)

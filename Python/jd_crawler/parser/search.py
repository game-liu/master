import json

from bs4 import BeautifulSoup


def parse_jd_item(html):
    result = []
    soup = BeautifulSoup(html, 'lxml')
    item_array = soup.select("ul[class='gl-warp clearfix'] li[class='gl-item']")
    for item in item_array:
        sku_id = item.attrs['data-sku']
        img = item.select("img[data-img='1']")
        price = item.select("div[class='p-price']")
        title = item.select("div[class='p-name p-name-type-2']")
        shop = item.select("div[class='p-shop']")
        icons = item.select("div[class='p-icons']")

        img = img[0].attrs['data-lazy-img'] if img else ""
        price = price[0].strong.i.text.strip() if price else ""
        title = title[0].text.strip().replace('\r\n', '').replace('\n', '').replace('\t', '').replace(' ','') if title else ""
        shop = shop[0].a.attrs['title'].strip().replace('\r\n', '').replace('\n', '').replace('\t', '') if shop else ""
        icons = json.dumps([tag_ele.text for tag_ele in icons[0].select('i')]) if icons else "[]"
        result.append((sku_id, img, price, title, shop, icons))
    return result


if __name__ == "__main__":
    with open("../test/search.html", 'r', encoding='utf-8') as f:
        html = f.read()
        result = parse_jd_item(html)
        print(result)

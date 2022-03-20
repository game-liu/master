import pymysql
import requests

from master.Python.jd_crawler.parser.search import parse_jd_item
from master.Python.jd_crawler.settings import HEADERS, MYSQL_CONF


def saver(item_array):
    """
    持久化爬取结果
    :param item_array:
    :return:
    """
    cursor = mysql_con.cursor()
    SQL = """INSERT INTO jd_search(sku_id, img, price, title, shop, icons)
            VALUES(%s,%s,%s,%s,%s,%s)"""
    cursor.executemany(SQL, item_array)
    mysql_con.commit()


def downloader(task):
    """
    请求目标网址的组件
    :param task:
    :return:
    """
    url = 'https://search.jd.com/Search'
    params = {
        "keyword": task
    }
    res = requests.get(url=url, params=params, headers=HEADERS)
    return res


def main(task_array):
    """
    爬虫任务调度
    :param task_array:
    :return:
    """
    for task in task_array:
        result = downloader(task)
        item_array = parse_jd_item(result.text)
        print(f"get items:{item_array}")
        saver(item_array)


if __name__ == "__main__":
    mysql_con = pymysql.connect(**MYSQL_CONF)

    # 用来代替生产者
    task_array = ['鼠标', '键盘', '显卡', '耳机']
    main(task_array)

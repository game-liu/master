import datetime
import random

import pymysql

from master.decorator.demo_3 import decorate

MYSQL_CONF = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "123456",
    "db": "liu"
}

# 链接数据库
mysql_con = pymysql.connect(**MYSQL_CONF)

# 真正执行语句的线程
mysql_cursor = mysql_con.cursor()


@decorate
def insert_one():
    for i in range(5, 10 ** 3):
        name = f"store_name_{i}"
        department = f"事业部_{random.randint(1, 10)}"
        amount = format(random.uniform(10 ** 2, 10 ** 4), '.2f')
        create_time = datetime.datetime.now()
        sql = f"""insert into store_perf(name,amount,department,create_time)
                 values('{name}',{amount},'{department}','{create_time}')"""
        print(sql)
        mysql_cursor.execute(sql)
        mysql_con.commit()


@decorate
def insert_many():
    values = []
    for i in range(10 ** 3, 10 ** 6):
        name = f"store_name_{i}"
        department = f"事业部_{random.randint(1, 10)}"
        amount = format(random.uniform(10 ** 1, 10 ** 4), '.2f')
        create_time = datetime.datetime.now()
        values.append((name, amount, department, create_time))

    print(values)
    sql = f"""insert into store_perf(name,amount,department,create_time)
                     values(%s,%s,%s,%s)"""

    mysql_cursor.executemany(sql, values)
    mysql_con.commit()


def get_stores():
    sql = """select * from store_perf"""
    mysql_cursor.execute(sql)
    fetch_data = mysql_cursor.fetchall()
    print(fetch_data)
    print(len(fetch_data))


def transaction():
    try:
        sql_1 = "delete from store_perf where name='store_name_5'"
        sql_2 = 'insert into store_perf(name)'
        mysql_cursor.execute(sql_1)
        mysql_cursor.execute(sql_2)
    except Exception as e:
        print(f"raise Exception:{e}")
        print('rollback')
        mysql_con.rollback()
    finally:
        mysql_con.commit()


if __name__ == "__main__":
    # all_time:11.87181043624878
    # insert_one()
    # all_time: 2.09995698928833
    # insert_many()
    # get_stores()
    transaction()

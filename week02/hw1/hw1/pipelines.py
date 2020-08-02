# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from scrapy.utils.project import get_project_settings


class Hw1Pipeline:
    def process_item(self, item, spider):
        settings = get_project_settings()
        dbInfo = settings.get("MYSQL_SETTINGS")
        print(dbInfo)
        db = ConnDB(dbInfo)
        result_list = item['result_list']
        item_values = [(item['name'], item['movie_type'], item['online_time']) for item in result_list]
        print(item_values)
        db.insert_many_items(item_values)


class ConnDB(object):
    def __init__(self, dbInfo):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']

    def insert_many_items(self, values):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        cur = conn.cursor()
        try:
            cur.executemany("insert into items_tbl(movie_name, movie_title, online_date) values(%s, %s, %s)", values)
            conn.commit()
            print("success")
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cur.close()
            conn.close()


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql


class QianqianmusicPipeline(object):
    def __init__(self):
        # mongo版插入数据库
        # self.mongoConn = pymongo.MongoClient('mongodb://zcb:123@localhost:27017/')
        # self.db = self.mongoConn.qianqian
        # self.col = self.db.music
        # mysql版插入数据库
        self.conn = pymysql.connect('localhost', 'root', 'zxcvbnm000', 'qianqian', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # self.col.insert(dict(item))
        # 将item转为dict
        dic = dict(item)
        # 定义表名
        table_name = 'music'
        # 拼接sql语句
        sql = '''insert into %s(%s) value(%s)''' % (table_name, ','.join([k for k in dic.keys()]), ','.join(['"' + str(v) + '"' for v in dic.values()]))
        # 执行sql语句
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        return item

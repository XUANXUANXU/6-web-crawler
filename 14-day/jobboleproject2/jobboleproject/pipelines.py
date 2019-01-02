# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

# #将数据写入json文件
# class JobboleprojectPipeline(object):
#
#     def __init__(self):
#         self.file = open('data.json','a+')
#
#     def open_spider(self,spider):
#         # 爬虫开启的时候调用，只调用一次
#         print('爬虫文件开始执行',spider.name)
#
#     def process_item(self, item, spider):
#         print('管道文件我来了')
#         # with open('data.json','a+') as file:
#         #     data = json.dumps(dict(item),ensure_ascii=False)+'\n'
#         #     file.write(data)
#         data = json.dumps(dict(item),ensure_ascii=False)+'\n'
#         self.file.write(data)
#
#         return item
#
#     def close_spider(self,spider):
#         # 爬虫结束的时候会调用，只调用一次
#         print('爬虫文件结束执行',spider.name)
#         self.file.close()

import pymongo
from jobboleproject.items import JobboleprojectItem
#将数据写入mongodb,将单个item，写入单个集合
# class JobboleprojectPipeline(object):
#
#     def __init__(self):
#         self.mongoConn = pymongo.MongoClient('localhost',27017)
#         #切换到指定的数据库中
#         self.db = self.mongoConn.scrapy1803
#         #获取到数据库下的集合
#         self.col = self.db.jobbole
#
#     def open_spider(self,spider):
#         # 爬虫开启的时候调用，只调用一次
#         print('爬虫文件开始执行',spider.name)
#
#     def process_item(self, item, spider):
#         print('管道文件我来了')
#         self.col.insert(dict(item))
#         #isinstance 判断某一个对象是否是某个类的实例
#         # if isinstance(item,JobboleprojectItem):
#         #     #　通过这个方法我们可以判断item属于哪个类，
#         #     # 然后执行不同的插入操作
#         #     print('JobboleprojectItem')
#         #
#         # elif isinstance(item,xxxx):
#         #
#         #     print('JobboleprojectItem')
#         return item
#
#     def close_spider(self,spider):
#         # 爬虫结束的时候会调用，只调用一次
#         print('爬虫文件结束执行',spider.name)

# #改造版,将配置信息写在配置文件里面
# class JobboleprojectPipeline(object):
#
#     def __init__(self,mongo_host,mongo_port,mongo_db):
#         self.mongoConn = pymongo.MongoClient(mongo_host,mongo_port)
#         #切换到指定的数据库中
#         self.db = self.mongoConn[mongo_db]
#         #获取到数据库下的集合
#         self.col = self.db.jobbole
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_host=crawler.settings.get('MONGODB_HOST'),
#             mongo_port=crawler.settings.get('MONGODB_PORT'),
#             mongo_db = crawler.settings.get('MONGODB_DB')
#         )
#
#     def open_spider(self,spider):
#         # 爬虫开启的时候调用，只调用一次
#         print('爬虫文件开始执行',spider.name)
#
#     def process_item(self, item, spider):
#         print('管道文件我来了')
#         self.col.insert(dict(item))
#         return item
#
#     def close_spider(self,spider):
#         # 爬虫结束的时候会调用，只调用一次
#         print('爬虫文件结束执行',spider.name)

#将数据插入mysql,将配置信息写在settings.py文件里面
import  pymysql

class JobboleprojectPipeline(object):

    def __init__(self,host,port,db,user,pwd):
        self.mysqlConn = pymysql.Connect(host=host,user=user,
                                         password=pwd,database=db,port=port,
                                         charset='utf8')
        self.cursor = self.mysqlConn.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            port = crawler.settings.get('MYSQL_PORT'),
            db = crawler.settings.get('MYSQL_DB'),
            user = crawler.settings.get('MYSQL_USER'),
            pwd = crawler.settings.get('MYSQL_PWD'),
        )

    def open_spider(self,spider):
        # 爬虫开启的时候调用，只调用一次
        print('爬虫文件开始执行',spider.name)

    def process_item(self, item, spider):
        print('管道文件我来了')
        sql = """
        INSERT INTO jobbole(coverImage,link)
        VALUES (%s,%s)
        """
        try:
            self.cursor.execute(sql,(item['coverImage'],item['link']))
            self.mysqlConn.commit()
        except Exception as err:
            print(err)
            self.mysqlConn.rollback()
        return item

    def close_spider(self,spider):
        # 爬虫结束的时候会调用，只调用一次
        print('爬虫文件结束执行',spider.name)
        #关闭游标和关闭连接
        self.cursor.close()
        self.mysqlConn.close()


class JobboleprojectPipeline1(object):
    def process_item(self, item, spider):
        print('管道文件我来了1')
        return item

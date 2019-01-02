# -*- coding: utf-8 -*-
# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html




# import pymongo
# from zhilianproject.items import ZhilianprojectItem,CompanyprojectItem
#
#
# class ZhilianprojectPipeline(object):
#     def __init__(self):
#         self.mongodbconn = pymongo.MongoClient('mongodb://xuan:zxcvbnm000@localhost:27017/')
#         self.db = self.mongodbconn.zhilian
#         self.coll = self.db.job_col
#         self.coll2 = self.db.company_col
#
#
#     def open_spider(self,spider):
#         print('爬虫文件开始执行', spider.name)
#
#     def process_item(self, item, spider):
#         print('执行')
#         if isinstance(item,ZhilianprojectItem):
#             self.coll.insert(dict(item))
#         elif isinstance(item,CompanyprojectItem):
#             self.coll2.insert(dict(item))
#         return item
#
#     def close_spider(self,spider):
#         print('爬虫文件结束执行', spider.name)




import pymysql
from zhilianproject.items import ZhilianprojectItem,CompanyprojectItem

class ZhilianprojectPipeline(object):
    def __init__(self):
        self.mysqlconn = pymysql.Connect('localhost','root','zxcvbnm000','zhilian',charset='utf8')
        self.mysqldb = self.mysqlconn.cursor()

    def open_spider(self,spider):
        print('爬虫文件开始执行', spider.name)

    def process_item(self, item, spider):
        print('执行')
        dict_item = dict(item)
        if isinstance(item,ZhilianprojectItem):
            table_name = 'job_table'
        elif isinstance(item,CompanyprojectItem):
            table_name = 'company_table'

        sql = '''insert into %s(%s) values(%s) ''' % (table_name, ','.join(dict_item.keys()),','.join(['%s']*len(dict_item)))
        print(sql)
        try:
            self.mysqldb.execute(sql,[value for key,value in dict_item.items()])
            self.mysqlconn.commit()
        except Exception as err:
            print(err)
            self.mysqlconn.rollback()
        return item

    def close_spider(self,spider):
        print('爬虫文件结束执行', spider.name)
        self.mysqlconn.close()
        self.mysqldb.close()
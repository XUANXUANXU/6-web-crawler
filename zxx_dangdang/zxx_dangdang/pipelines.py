# import pymysql
# class ZxxDangdangPipeline(object):
#     def __init__(self):
#         self.mysqlcon = pymysql.connect('localhost', 'root', 'zxcvbnm000', 'dangdang', charset="utf8")
#         self.cursor = self.mysqlcon.cursor()
#
#     def process_item(self, item,spider):
#         dic = dict(item)
#         table_name = 'dang_book'
#         sql = '''insert into %s(%s) value(%s) ''' % (table_name, ','.join([k for k in dic.keys()]), ','.join(['"' + str(v) + '"' for v in dic.values()]))
#         self.cursor.execute(sql)
#         self.mysqlcon.commit()
#         return item
#
#     def close_spider(self,spider):
#         self.mysqlcon.close()

import pymongo

class ZxxDangdangPipeline(object):
    def __init__(self):
        self.mongodb = pymongo.MongoClient('mongodb://xuan:zxcvbnm000@localhost:27017/')
        self.db = self.mongodb['dangdang']
        self.col = self.db['dang_book']

    def process_item(self, item,spider):
        self.col.insert(dict(item))
    def close_spider(self,spider):
        self.db.close()
        self.col.close()




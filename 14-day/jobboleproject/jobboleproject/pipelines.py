# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymongo

class JobboleprojectPipeline(object):
    def __init__(self):

        pass
    def start_proce(self):
        pass

    def process_item(self, item, spider):
        print('zxcvbnm')
        return item

    def close_proce(self):
        pass
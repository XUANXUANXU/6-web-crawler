# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    salary = scrapy.Field()
    companyName = scrapy.Field()
    address = scrapy.Field()
    workYears = scrapy.Field()
    degree = scrapy.Field()
    needPeople = scrapy.Field()
    jobInfo = scrapy.Field()
    companyUrl = scrapy.Field()
    jobUrl = scrapy.Field()

class CompanyprojectItem(scrapy.Item):
    companyName = scrapy.Field()
    peopleNum = scrapy.Field()
    companyType = scrapy.Field()
    companyInfo = scrapy.Field()
    jobLine = scrapy.Field()
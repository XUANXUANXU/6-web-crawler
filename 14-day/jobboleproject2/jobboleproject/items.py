# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JobboleprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #封面
    coverImage = scrapy.Field()
    #详情地址
    link = scrapy.Field()
    #详情内容
    content = scrapy.Field()
    #标题
    title = scrapy.Field()
    #评论量
    commentNum = scrapy.Field()
    #点赞量
    zanNum = scrapy.Field()
    #收藏量
    markNum = scrapy.Field()
    #标签
    tags = scrapy.Field()
    #发布时间
    publishTime = scrapy.Field()
    #作者
    author = scrapy.Field()



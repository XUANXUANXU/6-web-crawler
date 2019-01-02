# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QianqianmusicItem(scrapy.Item):
    name = scrapy.Field()
    singer = scrapy.Field()
    album = scrapy.Field()
    pub_date = scrapy.Field()
    pub_company = scrapy.Field()
    like_num = scrapy.Field()
    comment_num = scrapy.Field()
    share_num = scrapy.Field()
    lrc = scrapy.Field()
    pass

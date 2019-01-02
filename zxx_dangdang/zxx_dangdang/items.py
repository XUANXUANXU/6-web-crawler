# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZxxDangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zxx_two_class = scrapy.Field()
    zxx_three_class = scrapy.Field()
    zxx_picture = scrapy.Field()
    zxx_like = scrapy.Field()
    zxx_bookname = scrapy.Field()
    zxx_content = scrapy.Field()
    zxx_author = scrapy.Field()
    zxx_press = scrapy.Field()
    zxx_pubtime = scrapy.Field()
    zxx_ranking = scrapy.Field()
    zxx_comment = scrapy.Field()
    zxx_money = scrapy.Field()


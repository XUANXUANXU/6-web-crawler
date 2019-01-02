# -*- coding: utf-8 -*-
import scrapy
from zxx_dangdang.items import ZxxDangdangItem


class ZxxJobdangSpider(scrapy.Spider):
    name = 'zxx_jobdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://book.dangdang.com/']

    def parse(self, response):
        # 获取页面源码写入本地,为了找到三级分类
        # with open('1.html','w') as file:
        #     file.write(response.text)
        #获取人文下的所有三级图书列表的链接
        three_list = response.xpath('//div[@name="m403752_pid5374_5366_t9147"]/dl/dd/a/@href').extract()
        #遍历
        for three in three_list:
            yield scrapy.Request(three,callback=self.book_list)

    def book_list(self,response):
        # print(response.status)
        # print(response.url)
        # 获取图书详情的链接
        booklinks = response.xpath('//ul[@class="bigimg"]/li/a/@href').extract()
        # print(booklink)
        for booklink in booklinks:
            yield scrapy.Request(booklink,callback=self.xiang_book)
        #获取所有分类下的所有页
        allpages = response.xpath('//ul[@name="Fy"]/li/a/@href').extract()
        for allpage in allpages:
            page = 'http://category.dangdang.com' + allpage
            yield scrapy.Request(page,callback=self.book_list)

    def xiang_book(self,response):
        #获取详情页的数据
        item = ZxxDangdangItem()
        item['zxx_two_class'] = response.xpath('//div[@class="breadcrumb"]/a[2]/text()').extract_first()
        item['zxx_three_class'] = response.xpath('//div[@class="breadcrumb"]/a[3]/text()').extract_first()
        item['zxx_picture'] = response.xpath('//div[@class="pic"]/a[@class="img"]/img/@src').extract_first()
        item['zxx_like'] = response.xpath('//a[@class="btn_scsp"]/text()').extract_first()
        item['zxx_bookname'] = response.xpath('//div[@class="name_info"]/h1/text()').extract_first()
        item['zxx_content'] = response.xpath('//div[@class="name_info"]/h2//span/text()').extract()
        item['zxx_author'] = response.xpath('//span[@id="author"]/a[1]/text()').extract_first()
        item['zxx_press'] = response.xpath('//span[@dd_name="出版社"]/a/text()').extract_first()
        item['zxx_pubtime'] = response.xpath('//div[@class="messbox_info"]/span[3]/text()').extract_first()
        item['zxx_ranking'] = response.xpath('//div[@class="pinglun"]/span/span/text()').extract_first()
        item['zxx_comment'] = response.xpath('//a[@id="comm_num_down"]/text()').extract_first()
        item['zxx_money'] = response.xpath('//p[@id="dd-price"]/text()').extract_first()
        print(item)
        yield item






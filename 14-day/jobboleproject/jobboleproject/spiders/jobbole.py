# -*- coding: utf-8 -*-
import scrapy

# 爬虫文件继承自scrapy.Spider
class JobboleSpider(scrapy.Spider):
    # 爬虫名称
    name = 'jobbole'
    # 允许爬取得域
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/page/1/']

    def parse(self, response):
        print(response.status)
        print(response.url)
        # 二进制数据(获取响应内容)
        # print(response.body)
        # 字符串数据(获取响应内容)
        # print(response.text)

        # 图片 详情链接
        # articles = response.css('.post.floated-thumb')
        articles = response.xpath('//div[@class="post floated-thumb"]')
        # print(len(articles))
        for article in articles:
            coverimage = article.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first()

            detaillink = articles.xpath('./div[@class="post-thumb"]/a/@href').extract_first()
            print(coverimage,detaillink)
            yield scrapy.Request(detaillink,callback=self.parse_arctivedetail)
    def parse_arctivedetail(self,response):
        print(response.status)

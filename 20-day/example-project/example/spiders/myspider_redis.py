from scrapy_redis.spiders import RedisSpider
import scrapy
from example.items import bookItem

class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    #爬虫的名称
    name = 'myspider_redis'
    #设置一个key，从redis数据库中获取requests任务
    redis_key = 'myspider:start_urls'
    #设置允许爬取的域（一般采用这种方式去设置）
    allowed_domains = ['quanshuwang.com']

    #动态获取允许爬取的域
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        urls = response.xpath('//ul[@class="channel-nav-list"]//li/a/@href').extract()
        print(urls)
        for url in urls:
            yield scrapy.Request(url,callback=self.parse_book_list)
        #第一步，获取各个分类的起始url

    def parse_book_list(self,response):
        #获取小说详情的链接
        bookUrls = response.xpath('//a[@class="clearfix stitle"]/@href').extract()
        for bookurl in bookUrls:
            yield scrapy.Request(bookurl,callback=self.parse_book)
        #获取所有分类的所有页面数据
        nextPages = response.xpath('//div[@id="pagelink"]//a/@href').extract()

        for nexturl in nextPages:
            yield scrapy.Request(nexturl,callback=self.parse_book_list)

    def parse_book(self,response):
        #实例化一个item对像
        item = bookItem()
        item['tag'] = response.xpath('//div[@class="main-index"]/a[2]/text()').extract_first()
        item['title'] = response.xpath('//div[@class="main-index"]/text()').extract()
        item['desc'] = response.xpath('//div[@class="infoDetail"]/div/text()').extract()
        item['author'] = response.xpath('//div[@class="bookDetail"]//dl[2]/dd/text()').extract_first()

        yield item



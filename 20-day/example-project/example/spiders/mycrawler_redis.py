from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider
from example.items import bookItem


class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'
    allowed_domains = ['quanshuwang.com']

    rules = (
        # follow all links
        # http://www.quanshuwang.com/list/2_1.html
        Rule(LinkExtractor(allow=r'http://www.quanshuwang.com/list/\d+_\d+.html'),
             callback='parse_page',
             follow=True),
        #http://www.quanshuwang.com/book_163649.html
        Rule(LinkExtractor(allow=r'http://www.quanshuwang.com/book_\d+.html'),
             callback='parse_book',follow=True)

    )

    def parse_page(self, response):
        print(response.status)
        print(response.url)

    def parse_book(self,response):
        print(response.status)
        print(response.url)
        #实例化一个item对象
        item = bookItem()
        item['tag'] = response.xpath('//div[@class="main-index"]/a[2]/text()').extract_first()
        item['title'] = response.xpath('//div[@class="b-info"]/h1/text()').extract_first()
        item['desc'] = ''.join(response.xpath('//div[@class="infoDetail"]/div/text()').extract()).replace(' ','')
        item['author'] = response.xpath('//div[@class="bookDetail"]//dl[2]/dd/text()').extract_first()
        yield item



from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from example.items import bookItem

class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/']


    rules = [
        Rule(LinkExtractor(allow=r'http://www.quanshuwang.com/list/\d+_\d+.html'),
             callback='parse_directory',follow=True),
        Rule(LinkExtractor(allow=r'http://www.quanshuwang.com/book_\d+.html'),callback='parse_book')
    ]

    def parse_directory(self, response):
        print(response.url)
        # for div in response.css('.title-and-desc'):
        #     yield {
        #         'name': div.css('.site-title::text').extract_first(),
        #         'description': div.css('.site-descr::text').extract_first().strip(),
        #         'link': div.css('a::attr(href)').extract_first(),
        #     }

    def parse_book(self,response):
        #实例化一个item对像
        item = bookItem()
        item['tag'] = response.xpath('//div[@class="main-index"]/a[2]/text()').extract_first()
        item['title'] = response.xpath('//div[@class="main-index"]/text()').extract()
        item['desc'] = response.xpath('//div[@class="infoDetail"]/div/text()').extract()
        item['author'] = response.xpath('//div[@class="bookDetail"]//dl[2]/dd/text()').extract_first()

        yield item


        # print(response.status)
        # print(response.url)

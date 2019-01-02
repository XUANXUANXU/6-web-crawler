# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JobboleSpider(CrawlSpider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/page/1/']
    # http: // blog.jobbole.com / all - posts / page / 2 /
    # http: // blog.jobbole.com / 114261 /
    # follow是否跟进
    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=(),deny=(),allow_domains=(),deny_domains=(),restrict_xpaths=(),tags=(),attrs=(),restrict_css=(),strip=True)),
        Rule(LinkExtractor(allow=r'.*?all-posts/page/\d+/',
                           restrict_xpaths='//div[@class="navigation margin-20"]'
                           )
             )
    )


    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

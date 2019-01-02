# -*- coding: utf-8 -*-
import scrapy
from jobboleproject.items import JobboleprojectItem

#我们创建的爬虫文件继承自scrapy.Spider
class JobboleSpider(scrapy.Spider):
    #name爬虫名称
    name = 'jobbole'
    #允许爬取的域,如果获取的连接不在这个域下,这个连接会被过滤掉,
    #可以设置多个域
    allowed_domains = ['jobbole.com']
    #起始url,是一个列表,可以设置多个起始url
    start_urls = ['http://blog.jobbole.com/all-posts/page/1/']

    #response就是下载器，请求任务之后的响应结果
    # 在这个函数中做数据的解析和url的提取
    def parse(self, response):
        #获取响应状态
        print(response.status)
        #获取请求的url
        print(response.url)
        #获取响应的内容,二进制数据，要使用的话需要解码
        # print(response.body)
        #获取响应的内容(字符串)
        # print(response.text)
        # print(type(response.text))
        #提取目标数据

        #通过xpath获取数据
        articles = response.xpath('//div[@class="post floated-thumb"]')
        #通过css获取数据
        # articles = response.css('.post.floated-thumb')
        print(len(articles))


        for article in articles:
            #初始化item
            articleItem = JobboleprojectItem()
            #extract()[0] => extract_first()
            #获取封面图片
            articleItem['coverImage'] = article.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first()
            #获取详情地址
            articleItem['link'] = article.xpath('./div[@class="post-thumb"]/a/@href').extract_first()
            # print(coverImage,detailLink)
            # meta:可以传值，字典类型
            yield scrapy.Request(
                articleItem['link'],
                callback=self.parse_article_detail,
                meta={'item':articleItem}
            )
            
        
    def parse_article_detail(self,response):
        #解析文章信息
        # print(response.status)
        #取值
        item = response.meta['item']
        # 提取信息自己提取
        # 取值

        item['title'] = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first("")
        item['publishTime'] = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract_first(
            "").strip().replace("·", "").strip()
        # object_id = re.match(".*?(\d+).*", url).group(1)
        item['zanNum'] = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract_first("")

        # 收藏量
        markNum = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").re('\d+')
        if len(markNum) > 0:
            markNum = markNum[0]
        else:
            markNum = 0
        item['markNum'] = markNum
        print(markNum)

        # 评论量
        comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").re('\d+')
        if len(comment_nums) > 0:
            comment_nums = comment_nums[0]
        else:
            comment_nums = 0
        item['commentNum'] = comment_nums

        # 内容
        # item['content'] = response.xpath("//div[@class='entry']").extract_first("")

        # 过滤评论标签
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']//a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)
        item['tags'] = tags

        # 作者
        item['author'] = response.xpath('//div[@class="copyright-area"]/a/text()').extract_first()

        # 将获取的数据交给管道处理
        yield item

        print(item)








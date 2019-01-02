# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qianqianmusic.items import QianqianmusicItem
import json,re


class MusicSpider(CrawlSpider):
    name = 'music'
    allowed_domains = ['music.taihe.com']
    start_urls = ['http://music.taihe.com/top']

    # 通用爬虫匹配所有歌曲的url
    rules = (
        Rule(LinkExtractor(allow=r'http://music.taihe.com/song/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 获取歌曲id
        sing_id = response.url.split('/')[-1]
        # 拼接歌曲详情josn数据的url
        sing_info_url = 'http://music.taihe.com/data/tingapi/v1/restserver/ting?method=baidu.ting.song.baseInfo&songid={}&from=web'.format(sing_id)
        yield scrapy.Request(sing_info_url,callback=self.parse_sing_info)


    def parse_sing_info(self,response):


        # josn转换为dict
        info = json.loads(response.text)
        # 创建item
        item = QianqianmusicItem()
        # 名字
        item['name'] = info['content']['title'].strip()
        # 歌手
        item['singer'] = info['content']['author'].strip()
        # 专辑
        item['album'] = info['content']['album_title'].strip()
        # 发布日期
        item['pub_date'] = info['content']['publishtime'].strip()
        # 发行公司
        item['pub_company'] = info['content']['si_publishcompany'].strip()
        # 喜欢数
        item['like_num'] = info['content']['collect_num']
        # 评论数
        item['comment_num'] = info['content']['comment_num']
        # 分享数
        item['share_num'] = info['content']['share_num']
        # 歌词链接
        lrclink = info['content']['lrclink']
        if lrclink == '':
            item['lrc'] = 'null'
            yield item

        else:
            yield scrapy.Request(lrclink,callback=self.getlrc,meta={'item':item},dont_filter=True)


    def getlrc(self,response):
        item = response.meta['item']

        lrc = re.sub('\\s+', ',', re.sub("[A-Za-z0-9\!\%\[\]\,\。\:\.\t]", "", response.text))[1::]
        item['lrc'] = lrc
        yield item
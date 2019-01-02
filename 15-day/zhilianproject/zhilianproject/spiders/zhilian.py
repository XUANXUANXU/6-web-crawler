# -*- coding: utf-8 -*-
import scrapy
import json
from zhilianproject.items import ZhilianprojectItem,CompanyprojectItem
# https://fe-api.zhaopin.com/c/i/sou?start=120&pageSize=60&cityId=635&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%BA%E4%BA%8B%E4%B8%93%E5%91%98&kt=3&lastUrlQuery=%7B%22p%22:3,%22pageSize%22:%2260%22,%22jl%22:%22635%22,%22kw%22:%22%E4%BA%BA%E4%BA%8B%E4%B8%93%E5%91%98%22,%22kt%22:%223%22%7D

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=635&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%BA%E4%BA%8B%E4%B8%93%E5%91%98&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:%22635%22,%22kw%22:%22%E4%BA%BA%E4%BA%8B%E4%B8%93%E5%91%98%22,%22kt%22:%223%22%7D']

    def parse(self, response):
        print(response.status)
        # print(response.text)
        data = json.loads(response.text)
        print(type(data))
        jobList = data['data']['results']
        print(len(jobList))
        for job in jobList:
            jobitem = ZhilianprojectItem()
            jobitem['jobName'] = job['jobName']
            jobitem['salary'] = job['salary']
            jobitem['companyName'] = job['company']['name']
            # jobitem['address'] = job['']
            jobitem['workYears'] = job['workingExp']['name']
            jobitem['degree'] = job['eduLevel']['name']
            # jobitem['needPeople'] = job['']
            # jobitem['jobInfo'] = job['']
            jobitem['companyUrl'] = job['company']['url']
            jobitem['jobUrl'] = job['positionURL']
            # print(job)
            
            yield scrapy.Request(jobitem['jobUrl'],callback=self.parse_job_detail,meta={'item':jobitem})

    def parse_job_detail(self,response):
        with open('page.html','w') as file:
            file.write(response.text)
        jobitem = response.meta['item']
        jobitem['address'] = response.xpath('//div[@class="terminalpage-main clearfix"]//div[@class="tab-inner-cont"]//h2/text()').extract_first()
        needpeople = response.xpath('//ul[@class="terminal-ul clearfix"]/li[7]/strong/text()').re('\d+')
        if len(needpeople) > 0:
            jobitem['needPeople'] = needpeople[0]
        else:
            jobitem['needPeople'] = 0
        jobitem['jobInfo'] = ''.join(response.xpath('//div[@class="terminalpage-main clearfix"]//div[@class="tab-inner-cont"]//p//text()').extract()).replace('\n','')
        yield scrapy.Request(jobitem['companyUrl'],callback=self.parse_company)
        # print(jobitem)
        yield jobitem
    def parse_company(self,response):
        with open('company.html','w') as file:
            file.write(response.text)
        companyitem = CompanyprojectItem()
        # print(response.text)
        companyitem['companyName'] = str(response.xpath('//div[@class="mainLeft"]/div/h1/text()').extract_first()).replace('\r','').replace('\n','').strip()
        if not companyitem['companyName']:
            companyitem['companyName'] = 'null'
        companyitem['peopleNum'] = response.xpath('//table[@class="comTinyDes"]/tr[2]/td[2]/span/text()').extract_first()
        if not companyitem['peopleNum']:
            companyitem['peopleNum'] = 'null'
        companyitem['companyType'] = response.xpath('//table[@class="comTinyDes"]/tr[3]/td[2]/span/text()').extract_first()
        if not companyitem['companyType']:
            companyitem['companyType'] = 'null'
        companyitem['companyInfo'] = ''.join(response.xpath('//div[@class="part2"]/div[@class="company-content"]//text()').extract()).replace('\xa0','').replace('\r','').replace('\n','').strip()
        if not companyitem['companyInfo']:
            companyitem['companyInfo'] = 'null'
        # companyitem['jobLine'] = response.xpath('//li[@class="com-interview__item cursor-pointer"]/span[1]/text()').extract_first()
        # print(companyitem)
        yield companyitem













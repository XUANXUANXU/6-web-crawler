# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

#表示使用scrapy-redis自定义的去重组件，不使用scrapy框架自带的去重组件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#表示使用scrapy-redis自定义的调度器组件，不适用scrapy框架默认的调度器组件
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#　SCHEDULER_PERSIST设置为True,表示记录请求任务的状态，
# 下次再次运行会从上一次结束的位置开始
SCHEDULER_PERSIST = True

#scrapy-redis默认的队列类型，任务有优先级，采用的有序集合实现的
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#同样是队列类型，相当于栈的结构，先进后出（内部是双向链表实现的）
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#相当于堆的结构，先进先出，（内部是双向链表实现的）
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

#RedisPipeline将所有的item数据存放在redis数据库中
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

#设置你要连接的redis数据库的ip
REDIS_HOST = '192.168.43.33'
#设置你要连接的redis数据库的端口号
REDIS_PORT = 6379

#设置日志等级
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
#下载延时
DOWNLOAD_DELAY = 1

from django.db import models

# Create your models here.
class Qianqian(models.Model):
    name = models.CharField(max_length=255, verbose_name='名字')
    singer = models.CharField(max_length=255, verbose_name='歌手')
    album = models.CharField(max_length=255, verbose_name='专辑')
    pub_date = models.CharField(max_length=255, verbose_name='发行时间')
    pub_company = models.CharField(max_length=255, verbose_name='发布公司')
    like_num = models.CharField(max_length=255, verbose_name='喜欢数量')
    comment_num = models.CharField(max_length=255, verbose_name='评论数量')
    share_num = models.CharField(max_length=255, verbose_name='分享数量')
    lrc = models.TextField(verbose_name='歌词')

    class Meta:
        verbose_name = '千千音乐'
        verbose_name_plural = verbose_name
        db_table = 'music'
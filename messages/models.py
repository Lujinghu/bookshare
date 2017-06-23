from django.db import models


class Message(models.Model):
    receive_user_id = models.IntegerField(verbose_name='接收用户的id', default=0)
    text = models.TextField(verbose_name='消息内容', max_length=200)
    has_read = models.BooleanField(verbose_name='已读', default=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '消息'
        verbose_name_plural = verbose_name

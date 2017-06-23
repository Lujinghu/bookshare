from django.db import models


class Place(models.Model):
    name = models.CharField(verbose_name='地点名', max_length=100)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def get_books(self):
        if self.user_set is None:
            return None
        books = []
        for user in self.user_set:
            user_books = list(user.book_set.all())
            books.extend(user_books) #追加单个元素使用append， 追加一个列表使用extend
        return books
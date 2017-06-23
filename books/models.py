from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse


class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=50)
    author = models.CharField(verbose_name='作者', default='', max_length=50)
    image = models.ImageField(verbose_name='书籍图片', max_length=100, upload_to='books-image/%Y/%m')
    owner = models.ForeignKey(User, verbose_name='持有者')
    intro = models.TextField(verbose_name='推荐语', default='', max_length=500)
    is_available = models.BooleanField(verbose_name='是否可借', default=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    visited_times = models.IntegerField(verbose_name='浏览量', default=0)
    loaned_times = models.IntegerField(verbose_name='借出次数', default=0)
    created_time = models.DateTimeField(verbose_name='入库时间', auto_now_add=True)
    last_loan_time = models.DateTimeField(verbose_name='上次借出时间')

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def loan(self):
        if not self.is_available:
            return
        self.is_available = False
        self.loaned_times += 1
        self.last_loan_time = timezone.now()

    def book_return(self):
        if self.is_available:
            return
        self.is_available = True

    def get_absolute_url(self):
        return reverse('books:book_detail', (self.id, ))


class BookLoan(models.Model):
    #注意，看看能不能重写create方法
    book = models.ForeignKey(Book, verbose_name='书籍')
    loaner = models.ForeignKey(User, verbose_name='借阅人')
    created_time = models.DateTimeField('借阅开始时间', auto_now_add=True)
    back_time = models.DateTimeField('归还时间', null=True)




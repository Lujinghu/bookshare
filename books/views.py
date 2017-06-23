from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Book, BookLoan
from pure_pagination import Paginator, PageNotAnInteger
from .forms import BookCreateForm
from .decorators import check_book_owner_dec
from place.models import Place


class BookCreateView(View):

    @login_required()
    def get(self, request):
        form = BookCreateForm()
        context = {'form': form}
        return render(request, 'books/book_create.html', context)

    @login_required()
    def post(self, request):
        form = BookCreateForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            messages.success(request, '书籍{}已经添加入库!'.format(book.name))
            return redirect(reverse('books:book_manage'))
        else:
            context = {'form': form}
            return render(request, 'books/book_create.html', context)


class BookManageView(View):

    @login_required()
    def get(self, request):
        books = request.user.book_set.all().order_by('-created_time')
        #中间加入一些分页器
        context = {'books': books}
        return render(request, 'books/book_manage.html', context)


class BookListView(View):

    @login_required()
    def get(self, request, place_id):
        place = Place.objects.get(id=place_id)
        user_set = place.user_set.all()
        books = Book.objects.filter(user__in=user_set)
        context = {'books': books}
        return render(request, 'books/book_list.html', context)


class BookDeleteView(View):

    @check_book_owner_dec
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        #似乎根据我的实践，是不用使用int函数转换book_id的,是新版的django改进了吗
        if book.is_delete:
            book.delete()
            messages.success(request, '书籍{}已经被彻底删除'.format(book.name))
        else:
            book.is_delete = True
            book.save()
            messages.success(request, '书籍{}已经被下架'.format(book.name))
        return redirect(reverse('books:book_manage'))


class BookLoanView(View):

    @login_required()
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        user = request.user
        book.loan()
        bookloan = BookLoan.objects.create(book=book, loaner=user)
        messages.success(request, '书籍{}借阅成功！请阅读后按时归还'.format(book.name))
        return redirect(reverse('books:book_loaned'))


class BookReturnView(View):

    @login_required()
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book.book_return()
        messages.success(request, '书籍:{}已经被成功归还，欢迎下次继续借阅！'.format(book.name))
        return redirect(reverse('books:book_loaned'))


class BookEditView(View):

    @login_required()
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = BookCreateForm(book)
        context = {'form': form}
        return render(request, 'books/book_edit.html', context)

    @login_required()
    def post(self, request):
        form = BookCreateForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            messages.success(request, '书籍{}的信息已经修改成功!'.format(book.name))
            return redirect(reverse('books:book_manage'))
        else:
            context = {'form': form}
            return render(request, 'books/book_edit.html', context)


class BookDetailView(View):

    @login_required()
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        context = {'book': book}
        return render(request, 'books/book_detail.html', context)






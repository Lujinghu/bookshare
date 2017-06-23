from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^book_detail/(?<book_id>\d+)$', views.BookDetailView.as_view(), name='book_detail'),
    url(r'$book_delete/(?P<book_id>\d+)$', views.BookDeleteView.as_view(), name='book_delete'),
    url(r'^book_edit/(?P<book_id>\d+)$', views.BookEditView.as_view(), name='book_edit'),
    url(r'book_list/(?P<place_id>\d+)$', views.BookListView.as_view(), name='book_list'),
    url(r'^book_create/$', views.BookCreateView.as_view(), name='book_create'),
    url(r'^book_manage/$', views.BookManageView.as_view(), name='book_manage'),
    url(r'^book_loan/(?P<book_id>\d+)$', views.BookLoanView.as_view(), name='book_loan'),
    url(r'book_return/(?P<book_id>\d+)', views.BookReturnView.as_view(), name='book_return'),
]
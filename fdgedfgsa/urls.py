from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('readers/', views.ReaderListView.as_view(), name='reader-list'),
    path('readers/<int:pk>/', views.ReaderDetailView.as_view(), name='reader-detail'),
]
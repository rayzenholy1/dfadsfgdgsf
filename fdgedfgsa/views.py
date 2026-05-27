from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Book, Reader

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'fdgedfgsa/book_list.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        mode = self.request.GET.get('mode')
        if mode == 'available':
            queryset = queryset.filter(current_reader__isnull=True)
        # else show all
        return queryset

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'fdgedfgsa/book_detail.html'
    context_object_name = 'book'

class ReaderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Reader
    template_name = 'fdgedfgsa/reader_list.html'
    context_object_name = 'readers'
    permission_required = 'fdgedfgsa.view_reader'  # we'll need to set permissions
    
class ReaderDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Reader
    template_name = 'fdgedfgsa/reader_detail.html'
    context_object_name = 'reader'
    permission_required = 'fdgedfgsa.view_reader'
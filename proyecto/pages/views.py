from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PageListView(ListView):
    model = Page
    template_name = 'pages/list.html'


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'pages/create.html'
    success_url = reverse_lazy('pages')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'pages/update.html'
    success_url = reverse_lazy('pages')


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('pages')
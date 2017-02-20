from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import check_password, make_password

from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from hitcount.views import HitCountDetailView

from .models import Notice, Review, BeforeAfter, Counsel
from .forms import NoticeForm, ReviewForm, BeforeAfterForm, CounselForm

PAGINATION = 9


class CustomListView(ListView):
    paginate_by = PAGINATION  # default context_object_name: page_obj

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return self.model.objects.all().order_by('-updated_at')
        return self.model.objects.filter(show=True).order_by('-updated_at')


class CustomDetailView(HitCountDetailView):
    count_hit = True
    paginate_by = PAGINATION

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated():
            context['page_obj'] = self.model.objects.all().order_by('-updated_at')
        else:
            context['page_obj'] = self.model.objects.filter(show=True).order_by('-updated_at')

        paginator = Paginator(context['page_obj'], PAGINATION)
        page = self.request.GET.get('page')

        try:
            context['page_obj'] = paginator.page(page)
        except PageNotAnInteger:
            context['page_obj'] = paginator.page(1)
        except EmptyPage:
            context['page_obj'] = paginator.page(paginator.num_pages)

        return context


class CustomCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/blog_new.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        self.object = instance
        return redirect(self.get_success_url())


class CustomHideView(LoginRequiredMixin, ListView):
    paginate_by = PAGINATION  # default context_object_name: page_obj
    ordering = "-updated_at"

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(self.model, pk=self.kwargs['pk'])
        instance.show = not instance.show
        instance.save()
        return self.get(request, *args, **kwargs)


class CustomEditView(LoginRequiredMixin, UpdateView):
    fields = ['title', 'content']
    template_name = 'blog/blog_new.html'


class NoticeList(CustomListView):
    model = Notice
    template_name = 'blog/notice_list.html'


class NoticeDetail(CustomDetailView):
    model = Notice
    template_name = 'blog/notice_detail.html'


class NoticeCreate(CustomCreateView):
    model = Notice
    form_class = NoticeForm


class NoticeHide(CustomHideView):
    model = Notice
    template_name = 'blog/notice_list.html'


class NoticeDelete(LoginRequiredMixin, DeleteView):
    model = Notice
    success_url = reverse_lazy('blog:notice_list')


class NoticeUpdate(CustomEditView):
    model = Notice


class ReviewList(CustomListView):
    model = Review
    template_name = 'blog/review_list.html'


class ReviewDetail(CustomDetailView):
    model = Review
    template_name = 'blog/review_detail.html'


class ReviewCreate(CustomCreateView):
    model = Review
    form_class = ReviewForm


class ReviewHide(CustomHideView):
    model = Review
    template_name = 'blog/review_list.html'


class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('blog:review_list')


class ReviewUpdate(CustomEditView):
    model = Review


class BeforeAfterList(CustomListView):
    model = BeforeAfter
    template_name = 'blog/beforeafter_list.html'


class BeforeAfterDetail(CustomDetailView):
    model = BeforeAfter
    template_name = 'blog/beforeafter_detail.html'


class BeforeAfterCreate(CustomCreateView):
    model = BeforeAfter
    form_class = BeforeAfterForm


class BeforeAfterHide(CustomHideView):
    model = BeforeAfter
    template_name = 'blog/beforeafter_list.html'


class BeforeAfterDelete(LoginRequiredMixin, DeleteView):
    model = BeforeAfter
    success_url = reverse_lazy('blog:beforeafter_list')


class BeforeAfterUpdate(CustomEditView):
    fields = ['title', 'content', 'image']
    model = BeforeAfter


class CounselList(CustomListView):
    model = Counsel
    template_name = 'blog/counsel_list.html'


class CounselDetail(CustomDetailView):
    model = Counsel
    template_name = 'blog/counsel_detail.html'


class CounselCreate(CustomCreateView):
    model = Counsel
    form_class = CounselForm


class CounselHide(CustomHideView):
    model = Counsel
    template_name = 'blog/counsel_list.html'


class CounselDelete(LoginRequiredMixin, DeleteView):
    model = Counsel
    success_url = reverse_lazy('blog:counsel_list')


class CounselUpdate(CustomEditView):
    model = Counsel

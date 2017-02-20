from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from blog.model_rename import RenameFile

from hitcount.models import HitCountMixin
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from django_unique_slugify import unique_slugify as uslug


class BoardMixin(HitCountMixin, models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Notice(BoardMixin):
    class Meta:
        verbose_name = '공지/이벤트'
        verbose_name_plural = '공지/이벤트'

    def get_absolute_url(self):
        return reverse('blog:notice_detail', kwargs={'pk': self.pk})


class Review(BoardMixin):
    class Meta:
        verbose_name = '고객후기'
        verbose_name_plural = '고객후기'

    def get_absolute_url(self):
        return reverse('blog:review_detail', kwargs={'pk': self.pk})


class Counsel(BoardMixin):
    class Meta:
        verbose_name = '온라인 상담'
        verbose_name_plural = '온라인 상담'

    def get_absolute_url(self):
        return reverse('blog:counsel_detail', kwargs={'pk': self.pk})


class BeforeAfter(BoardMixin):
    image = ImageField(upload_to=RenameFile('images/'))

    class Meta:
        verbose_name = '전후사진'
        verbose_name_plural = '전후사진'

    def get_absolute_url(self):
        return reverse('blog:beforeafter_detail', kwargs={'pk': self.pk})

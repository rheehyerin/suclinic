from django import forms
from .models import Notice, Review, BeforeAfter, Counsel
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NoticeForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Notice
        fields = ['title', 'content']
        labels = {
            'title': '제목 (필수, 50자 이내)',
            'content': '내용 (필수)',
        }


class ReviewForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Review
        fields = ['title', 'content']
        labels = {
            'title': '제목 (필수, 50자 이내)',
            'content': '내용 (필수)',
        }


class CounselForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Counsel
        fields = ['title', 'content']
        labels = {
            'title': '제목 (필수, 50자 이내)',
            'content': '내용 (필수)',
        }


class BeforeAfterForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BeforeAfter
        fields = ['title', 'content', 'image']
        labels = {
            'title': '제목 (필수, 50자 이내)',
            'content': '내용 (필수)',
            'image': '썸네일 이미지',
        }

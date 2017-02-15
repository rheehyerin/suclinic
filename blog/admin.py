from django.contrib import admin
from .models import Notice, BeforeAfter, Counsel, Review
# Register your models here.
admin.site.register(Counsel)
admin.site.register(BeforeAfter)
admin.site.register(Notice)
admin.site.register(Review)

from django.contrib import admin
from .models import Review, Movie, Community, Comment, ReviewComment
# Register your models here.

admin.site.register(Review)
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(ReviewComment)


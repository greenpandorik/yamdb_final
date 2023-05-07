from django.contrib import admin

from .models import Comment, Genre, Review, Title, Category

admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Comment)

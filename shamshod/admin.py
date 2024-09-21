from django.contrib import admin
from .models import Category, Tag, Article, Contact, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    prepopulated_fields = {"slug":["name"]}



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_active', 'created_at')
    readonly_fields = ('views', )
    prepopulated_fields = {"slug":["title"]}
    readonly_fields = ('created_at', 'updated_at')

    filter_horizontal = ('tags',)


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')



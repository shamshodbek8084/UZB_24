from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Article, Category
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


class HomeView(View):
    def get(self, request):
        
        # categories = Category.objects.all()
        articles = Article.objects.all()
        main_news = articles[:4]
        featured_news = articles.order_by("?")[:4]
        latest_news = articles.order_by("-id")[:6]
        entertainment_post = articles.order_by("?")[:4]
        business_post = articles.order_by("?")[:4]
        travel_post = articles.order_by("?")[:4]
        all_news = articles[:12]

        context = {
            "main_news":main_news,
            "featured_news":featured_news,
            "latest_news":latest_news,
            "entertainment_post":entertainment_post,
            "business_post":business_post,
            "travel_post":travel_post,
            "all_news":all_news
        }
        return render(request, 'index.html', context)
    

class ArticleDetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        article.views+=1
        article.save()

        similiar_news = Article.objects.filter(category=article.category).exclude(slug=slug).order_by("?")[:4]

        context = {
            "article":article,
            "similiar_news":similiar_news
        }
        return render(request, 'blog_detail_02.html', context)
    
class CategoryView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        category_news = Article.objects.filter(category=category).order_by("?")[:12]


        context = {
            "category_news":category_news
        }
        return render(request, 'category_1.html', context)




class ContactView(View):
    form_class = ContactForm
    def get(self, request):
        
    
        return render(request, 'contact.html')
    
    def post(self, request):
        data = request.POST
        # print(data)
        form = self.form_class(data=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz Yuborildi")
            return redirect("contact")
        messages.error(request, "Nimadir xato")
        return render(request, 'contact.html')
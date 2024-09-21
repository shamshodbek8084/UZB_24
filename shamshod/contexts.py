from .models import Category,Tag, Article

def get_main_context(request):
    articles = Article.objects.all()
    main_news = articles[:4]
    categories = Category.objects.all()
    Tags = Tag.objects.all()
    trend_news = Article.objects.all().order_by("-views")[:4]
    context = {

        "categories":categories,
        "Tags":Tags,
        "trend_news":trend_news,
        "main_news":main_news,
        

    }
    return context



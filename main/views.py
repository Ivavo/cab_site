from django.shortcuts import render
from .models import Blog, Procedures


def about(request):
    return render(request, 'main/about_us.html')


def blog_page(request):
    blog = Blog.objects.order_by('-posted_date')
    return render(request, 'main/blog.html',
                  {'scroll': blog}
                  )


def add_blog_article(request):
    return render(request, 'main/add_blog_article.html')


def record(request):
    procedures = Procedures.objects.all()
    return render(request, 'main/records_page.html', {'procedures': procedures})


def services(request):
    procedures = Procedures.objects.all()
    return render(request, 'main/services.html',
                  {'service': procedures})


def articlepage(request):
    pass


def method():
    pass


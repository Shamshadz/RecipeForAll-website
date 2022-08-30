import random
from django.http import HttpResponse,Http404
from django.template.loader import render_to_string
from articles.models import Article
from django.shortcuts import render, redirect


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Justin" # hard coded
    random_id = random.randint(1, 4) # pseudo random
    
    # from the database??
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
    }
    # Django Templates
    HTML_STRING = render_to_string("articles/home_view.html", context=context)
    # HTML_STRING = """
    # <h1>{title} (id: {id})!</h1>
    # <p>{content}!</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)

def article_detail_view(request, slug=None):
    article_obj = None
    if id is not None:
            article_obj = Article.objects.get(id = id)
        
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)
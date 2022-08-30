from multiprocessing import context
import random
from django.http import HttpResponse,Http404
from django.template.loader import render_to_string
from articles.models import Article
from django.shortcuts import render, redirect

def article_create_view(request):

    

    return render(request,'articles/create.html',context)

def article_search_view(request):
    query_dict = request.GET   
    # query = query_dict.get("p")    <input type="text" name="q">
    try:
        query = int(query_dict.get("q"))   
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id = query)
    context =  {"object" : article_obj}
    return render(request,'articles/search.html',context=context)

def home_view(request):

    name = "Justin" # hard coded
    random_id = random.randint(1, 4) # pseudo random
    
    # from the database??
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()

    context = {
        "object_list": article_queryset,
        "object": article_obj,
    }
  
    return render(request,"home_view.html", context=context)

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
        
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)
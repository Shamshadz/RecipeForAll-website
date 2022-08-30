from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home_view'),
    path('articles/',views.article_search_view),
    path('articles/create/',views.article_create_view),
    path('articles/<int:id>/',views.article_detail_view),
]

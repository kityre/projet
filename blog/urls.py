from django.urls import path

from . import views


app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>', views.show, name='show'),
    path('article/', views.showArticle, name='showArticle'),
    path('customer/inscription', views.inscription, name='inscription'),

]

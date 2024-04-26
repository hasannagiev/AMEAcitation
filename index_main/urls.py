from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='details_view'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    # path('xeberler/', views.xeberler),
]


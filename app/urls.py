from django.conf.urls import url
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:articleId>/', views.article, name='article'),
    path('songs', views.song, name='songs')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
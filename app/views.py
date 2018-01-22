from django.shortcuts import render

from app.controller.articleController import ArticleController
from app.controller.songController import SongController

def index(request):
    articleCount = ArticleController.getArticleCount()
    # articleCount = 3
    articleList = ArticleController.getArticleListWithoutText()
    context = {'menu':'article','articleCount': articleCount, 'articleList':articleList}
    return render(request, 'Nostory/articleList.html', context)

def article(request, articleId):
    articleDetail = ArticleController.getArticle(articleId)
    context = {'menu':'article', 'article' : articleDetail}
    return render(request, 'Nostory/articleDetail.html', context)

def song(request):
    songList = SongController.getSongList()
    context = {'menu':'music', 'songList' : songList}
    return render(request, 'Nostory/songList.html', context)
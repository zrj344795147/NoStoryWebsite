from app.models import Article

class ArticleController:
    def getArticleCount():
        return Article.objects.count()

    def getArticleListWithoutText(page=0, count=10):
        # articleList = Article.objects.all()[page:count]
        articleList = Article.objects.order_by('lastModifiedTime').values('id', 'title',
                                'abstraction', 'writer', 'createdTime', 'views')[page:count]
        for article in articleList:
            article['date'] = article['createdTime'].date()
            if len(article['abstraction']) > 400:
                article['abstraction'] = article['abstraction'][0:400] + ' ...';
        return articleList

    def getArticle(id):
        article = Article.objects.get(id=id)
        article.views += 1;
        article.save();
        article.date= article.createdTime.date()
        return article

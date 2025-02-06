from django.http import HttpResponse
import random
from django.template.loader import render_to_string

from articles.models import Article




def home_view(request):

    random_id = random.randint(1, 3)

    articles_queryset = Article.objects.all()

    # article_obj = Article.objects.get(id=random_id)

    context = {
        "articles_list": articles_queryset,
        # "id": article_obj.id,
        # "title": article_obj.title,
        # "content": article_obj.content
    }

    HTML_STRING = render_to_string("home_view.html", context)

     
    return HttpResponse(HTML_STRING)
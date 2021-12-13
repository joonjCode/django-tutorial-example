from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    article_obj = Article.objects.get(id=1)
    article_qs = Article.objects.all()
    # my_list = [102, 13, 342, 1331, 213]
    # my_list_str = "-".join(str(i) for i in my_list)
    # context = {"my_list_str": my_list_str}
    context = {
        "object_list": article_qs,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }
    html_strting = render_to_string("home-view.html", context=context)
    return HttpResponse(html_strting)

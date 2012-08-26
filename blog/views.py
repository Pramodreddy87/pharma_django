from blog.models import Articles as mArticles
from django.shortcuts import render_to_response
def index(request):
    articles=mArticles.objects.all().order_by('id')[:10]
    return render_to_response('index.html',{'entries':articles})


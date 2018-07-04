from django.urls import path, include
from django.views.generic import Listview, Detailview
from blog.models import Post

urlpatterns = [path('', Listview.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/blog.html"))]

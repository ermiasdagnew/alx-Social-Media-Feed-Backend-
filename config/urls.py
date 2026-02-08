from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("API is running")  # ✅ root URL text

urlpatterns = [
    path("", home),  # root URL
    path("admin/", admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("api/", include("feed.urls")),
]

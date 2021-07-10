from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Home, name="home"),
    path("users/", include("users.urls")),
    path('articles/', include('articles.urls')),
    path('about/', views.About, name="about" )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

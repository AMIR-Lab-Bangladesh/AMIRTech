
from django.contrib import admin
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/token/',  include('djoser.urls.jwt')),
    path('team/', include('apps.team.urls')),
    path('blog/', include('apps.blog.urls')),

]


from django.contrib import admin
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/token/',  include('djoser.urls.jwt')),
    path('team/', include('apps.team.urls')),
    path('blog/', include('apps.blog.urls')),
    path('designation/', include('apps.designation.urls')),
    path('experience/', include('apps.experience.urls')),
    path('education/', include('apps.education.urls')),
    path('sociallink/', include('apps.socialLink.urls')),
    path('tools/', include('apps.tools.urls')),
    path('product/', include('apps.products.urls')),
    path('cart/', include('apps.cart.urls')),
    path('applicant/', include('apps.applicant.urls')),

]

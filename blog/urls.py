from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import  settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view, name='home'),
    path('remerciements/', views.remerciements_view, name='remerciements'),
    path('contact/',include('Contact.urls'), name='contact'),
    # path('projets/',include('st_users.urls'), name='st_users'),
    path('projets/',include('projets.urls'), name='projets'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

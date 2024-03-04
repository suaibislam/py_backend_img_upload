from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        # path ('', views.index, name='index'),
        path ('insert', views.insert, name='insert'),
        path ('update/<id>', views.updateData, name='updateData'),
        path ('delete/<id>', views.deleteData, name='deleteData'),
        path('', views.home),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
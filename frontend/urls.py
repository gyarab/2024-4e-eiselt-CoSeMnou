from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# definice url adres
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('school_list/', views.school_list, name='school_list'),
    path('schools/<int:pk>/', views.school_detail, name='school_detail'),
    path('compare/', views.compare_results, name='compare_results'),
]
# obsluha statickych souboru
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
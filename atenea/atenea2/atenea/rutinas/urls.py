from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.InstructorListView.as_view(), name='instructor_list'),
    url(r'^instructor/(?P<pk>\d+)$', views.RutinaListView.as_view(), name='rutina_list'),
    url(r'^instructor/(?P<pk>\d+)/sexo/$', views.SexoListView.as_view(), name='sexo_list'),
    url(r'^instructor/(?P<pk>\d+)$', views.RutinaListView.as_view(), name='rutina_list'),
    url(r'^detail/(?P<pk>\d+)$', views.InstructorDetailView.as_view(), name='instructor_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
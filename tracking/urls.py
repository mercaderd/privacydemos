from django.urls import path

from . import views

app_name = 'tracking'
urlpatterns = [
    path('fp/', views.FingerprintView.as_view(), name='fingerprint'),
    path('fp/<slug:fp>/', views.DetailView.as_view(), name='detail'),
    path('etag/', views.EtagView.as_view(), name='etag'),
]
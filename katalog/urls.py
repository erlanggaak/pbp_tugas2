from django.urls import path, include
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    #path('katalog/', include('katalog.urls')),
]
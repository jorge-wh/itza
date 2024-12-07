# django packages
from django.urls import path, include
# local packages
from itza.apps.users.views.hello_world_views import index


urlpatterns = [
    path('', index, name='hello_world'),
    path('accounts/', include('allauth.urls')),
]

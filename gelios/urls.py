from django.urls import path, include
from rest_framework import routers

from gelios.views import UsersViewSet, UnitsViewSet

app_name = 'gelios'


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', UsersViewSet)
router.register(r'units', UnitsViewSet)
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls

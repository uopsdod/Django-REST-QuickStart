from django.urls import include, path
from rest_framework import routers
from .quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users001', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'groups001', views.GroupViewSet)
router.register(r'profile', views.ProfileViewSet, basename='MyModal')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
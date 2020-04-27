from rest_framework import routers
from .api import MainViewSet

router = routers.DefaultRouter()
router.register('api/main', MainViewSet, 'main')

urlpatterns = router.urls
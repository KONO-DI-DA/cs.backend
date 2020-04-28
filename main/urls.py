from rest_framework import routers
from .api import PlayersViewSet

router = routers.DefaultRouter()
router.register('api/players', PlayersViewSet, 'players')

urlpatterns = router.urls
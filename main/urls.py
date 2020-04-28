from rest_framework import routers
from .api import PlayersViewSet, RoomViewSet, ItemsViewSet, SeasonViewSet

router = routers.DefaultRouter()
router.register('api/players', PlayersViewSet, 'players')
router.register('api/room', RoomViewSet, 'room')
router.register('api/items', ItemsViewSet, 'items')
router.register('api/season', SeasonViewSet, 'season')


urlpatterns = router.urls
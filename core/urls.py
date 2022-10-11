import core.views
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register('tags', core.views.TagViewSet, basename='tag')
urlpatterns += router.urls
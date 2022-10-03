from django.contrib import admin
from django.urls import path
import core.views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', core.views.Index.as_view()),
    # path('tags/', core.views.Tags.as_view()),
    # path('tags/<pk>/', core.views.Tag.as_view()),
    path('persons/', core.views.Person.as_view()),
    path('persons/<int:id>/', core.views.person),
]

router = DefaultRouter()
router.register('tags', core.views.TagViewSet, basename='tag')
router.register('items', core.views.ItemViewSet, basename='items')
urlpatterns += router.urls
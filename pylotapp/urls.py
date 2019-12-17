from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageDetailView, PageDetail, PagesListView

router = DefaultRouter()
#router.register(r'pages', PageDetailView)
router.register('page', PageDetail)
router.register(r'pages',PagesListView, PageDetail)
urlpatterns = router.urls
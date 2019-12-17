from rest_framework import viewsets
from django.utils.decorators import method_decorator
from .models import Page, ContentVideo, ContentText, ContentAudio
from .serializers import PageDetailSerializer, PagesListSerializer
from .decor import countedPage

class PageDetailView(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    class_serializer = PageDetailSerializer
    def get_serializer_class(self):
        return PageDetailSerializer

class PagesListView(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    class_serializer = PagesListSerializer
    def get_serializer_class(self):
        return PagesListSerializer

@method_decorator(countedPage, name='dispatch')
class PageDetail(PageDetailView):
    model = Page

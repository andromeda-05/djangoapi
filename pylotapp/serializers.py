from rest_framework import serializers

from .models import Page, ContentVideo, ContentText, ContentAudio


class ContentVideoDetailSerializer(serializers.ModelSerializer):
    pageid = serializers.PrimaryKeyRelatedField(queryset=Page.objects.all(), source='page.id')
    class Meta:
        model = ContentVideo
        fields = '__all__'


class ContentAudioDetailSerializer(serializers.ModelSerializer):
    pageid = serializers.PrimaryKeyRelatedField(queryset=Page.objects.all(), source='page.id')
    class Meta:
        model = ContentAudio
        fields = '__all__'


class ContentTextDetailSerializer(serializers.ModelSerializer):
    pageid = serializers.PrimaryKeyRelatedField(queryset=Page.objects.all(), source='page.id')
    class Meta:
        model = ContentText
        fields = '__all__'



class PageDetailSerializer(serializers.ModelSerializer):
    contentvideo = ContentVideoDetailSerializer(many=True, read_only=True)
    contentaudio = ContentAudioDetailSerializer(many=True, read_only=True)
    contenttext = ContentTextDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = '__all__'

class PagesListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Page
        exclude = ['title','counter']



from django.contrib import admin
from .models import Page, ContentText, ContentVideo, ContentAudio


class ContentTextInLine(admin.StackedInline):
    model = ContentText
    extra = 0
    verbose_name = 'Текст'
    verbose_name_plural = 'Тексты'

class ContentVideoInLine(admin.StackedInline):
    model = ContentVideo
    extra = 0
    verbose_name = 'Видео'
    verbose_name_plural = 'Видео'

class ContentAudioInLine(admin.StackedInline):
    model = ContentAudio
    extra = 0
    verbose_name = 'Аудио'
    verbose_name_plural = 'Аудио'

class PageInLine(admin.ModelAdmin):
    inlines = [ContentTextInLine,
               ContentVideoInLine,
               ContentAudioInLine]
    verbose_name = 'Страница'
    verbose_name_plural = 'Страницы'

admin.site.register(Page, PageInLine,)
admin.site.register(ContentText)
admin.site.register(ContentVideo)
admin.site.register(ContentAudio)

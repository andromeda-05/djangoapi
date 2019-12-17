from django.conf import settings
from django.db import models
from django.utils import timezone

class Page (models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    counter = models.PositiveIntegerField(verbose_name='Счетчик', default=0)

class ContentText (models.Model):
    title = models.CharField(max_length= 200, verbose_name='Заголовок')
    counter = models.PositiveIntegerField(verbose_name='Счетчик', default=0)
    text = models.TextField(verbose_name='Текст')
    page = models.ForeignKey(Page, on_delete=models.CASCADE,verbose_name='Страница', related_name='contenttext' )

class ContentVideo(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    counter = models.PositiveIntegerField(verbose_name='Счетчик', default=0)
    urlVideo = models.URLField(verbose_name='URL Видео')
    urlSub = models.URLField(verbose_name='URL Субтитров')
    page = models.ForeignKey(Page, on_delete=models.CASCADE,verbose_name='Страница', related_name='contentvideo')


class ContentAudio(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    counter = models.PositiveIntegerField(verbose_name='Счетчик', default=0)
    urlAudio = models.URLField(verbose_name='URL Аудио')
    page = models.ForeignKey(Page, on_delete=models.CASCADE,verbose_name='Страница', related_name='contentaudio')
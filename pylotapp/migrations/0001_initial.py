# Generated by Django 2.2.7 on 2019-11-21 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('counter', models.PositiveIntegerField(blank=True, editable=False, verbose_name='Счетчик')),
            ],
        ),
        migrations.CreateModel(
            name='ContentVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('counter', models.PositiveIntegerField(blank=True, editable=False, verbose_name='Счетчик')),
                ('urlVideo', models.URLField(verbose_name='URL Видео')),
                ('urlSub', models.URLField(verbose_name='URL Субтитров')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pylotapp.Page', verbose_name='Страница')),
            ],
        ),
        migrations.CreateModel(
            name='ContentText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('counter', models.PositiveIntegerField(blank=True, editable=False, verbose_name='Счетчик')),
                ('text', models.TextField(verbose_name='Текст')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pylotapp.Page', verbose_name='Страница')),
            ],
        ),
        migrations.CreateModel(
            name='ContentAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('counter', models.PositiveIntegerField(blank=True, editable=False, verbose_name='Счетчик')),
                ('urlAudio', models.URLField(verbose_name='URL Аудио')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pylotapp.Page', verbose_name='Страница')),
            ],
        ),
    ]

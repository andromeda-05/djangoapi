# Generated by Django 2.2.7 on 2019-11-23 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pylotapp', '0005_auto_20191123_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentaudio',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contentaudio', to='pylotapp.Page', verbose_name='Страница'),
        ),
        migrations.AlterField(
            model_name='contenttext',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contenttext', to='pylotapp.Page', verbose_name='Страница'),
        ),
        migrations.AlterField(
            model_name='contentvideo',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contentvideo', to='pylotapp.Page', verbose_name='Страница'),
        ),
    ]

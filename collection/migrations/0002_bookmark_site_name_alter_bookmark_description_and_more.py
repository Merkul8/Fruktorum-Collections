# Generated by Django 4.2.8 on 2023-12-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='site_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название сайта'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.TextField(blank=True, max_length=3000, verbose_name='Краткое описания'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='og_image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото Open Graph'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название'),
        ),
    ]

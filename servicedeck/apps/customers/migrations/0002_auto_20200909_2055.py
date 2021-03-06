# Generated by Django 3.1 on 2020-09-09 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('works', '0002_auto_20200909_2055'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='phone',
            field=models.CharField(blank=True, help_text='Phone', max_length=15, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='works',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.work', verbose_name='Works'),
        ),
    ]

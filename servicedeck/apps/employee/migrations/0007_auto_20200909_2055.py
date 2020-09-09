# Generated by Django 3.1 on 2020-09-09 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_delete_employeework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='kpi',
            field=models.FloatField(default=0, help_text='KPI', verbose_name='KPI'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='employee_images', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='position',
            name='responsibilities',
            field=models.TextField(verbose_name='Responsibilities'),
        ),
        migrations.AlterField(
            model_name='position',
            name='status',
            field=models.CharField(choices=[('D', 'Director'), ('CE', 'Chief Engineer'), ('LS', 'Line Specialist')], max_length=2, verbose_name='Status'),
        ),
    ]

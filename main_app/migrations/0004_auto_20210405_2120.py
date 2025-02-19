# Generated by Django 3.1.6 on 2021-04-05 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('main_app', '0003_auto_20210402_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='content_type_images', to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]

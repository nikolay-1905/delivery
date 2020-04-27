# Generated by Django 3.0.5 on 2020-04-27 11:31

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20200427_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '150x150', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=image_cropping.fields.ImageCropField(blank=True, null=True, upload_to='product'),
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-15 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='order',
        ),
        migrations.AddField(
            model_name='notification',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.OrderProduct'),
        ),
    ]

# Generated by Django 3.1.3 on 2023-09-20 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20230920_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bioequivalente',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

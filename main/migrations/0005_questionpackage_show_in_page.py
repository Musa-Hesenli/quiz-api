# Generated by Django 3.1.7 on 2021-07-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210706_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpackage',
            name='show_in_page',
            field=models.BooleanField(default=False),
        ),
    ]

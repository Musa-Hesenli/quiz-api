# Generated by Django 3.1.7 on 2021-07-06 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_customercreatedquizes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerCreatedQuizes',
            new_name='CustomerCreatedQuiz',
        ),
    ]

# Generated by Django 5.1.1 on 2025-04-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-24 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='sentiment',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
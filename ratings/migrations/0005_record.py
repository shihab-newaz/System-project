# Generated by Django 4.1.4 on 2022-12-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_alter_review_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(default='', max_length=255)),
                ('bought_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

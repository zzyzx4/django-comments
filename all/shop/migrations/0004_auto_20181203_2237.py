# Generated by Django 2.1.2 on 2018-12-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_commentary'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='created',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Модерация'),
        ),
    ]
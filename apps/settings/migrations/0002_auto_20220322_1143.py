# Generated by Django 3.2.7 on 2022-03-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='tel',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.5 on 2021-12-22 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humancounter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='OutputImage',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='OutputVideo',
            field=models.CharField(default='a', max_length=100),
        ),
    ]

# Generated by Django 3.2.9 on 2022-01-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
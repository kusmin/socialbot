# Generated by Django 4.0.5 on 2022-06-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='categoria',
        ),
        migrations.AddField(
            model_name='tag',
            name='categoria',
            field=models.ManyToManyField(to='tag.categoria'),
        ),
    ]

# Generated by Django 4.2.16 on 2024-12-02 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communities',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]

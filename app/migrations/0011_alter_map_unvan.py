# Generated by Django 4.1.7 on 2023-05-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_map_tel1_alter_map_tel2_alter_map_tel3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='unvan',
            field=models.CharField(max_length=255, verbose_name='Unvan'),
        ),
    ]

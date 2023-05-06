# Generated by Django 4.2 on 2023-04-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarix', models.DateField(auto_created=True, verbose_name='Tarix')),
                ('title', models.CharField(max_length=250, verbose_name='Başlıq')),
                ('photo', models.ImageField(upload_to='products/', verbose_name='Şəkil')),
                ('metn', models.TextField(verbose_name='Mətn')),
            ],
        ),
    ]

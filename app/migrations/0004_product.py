# Generated by Django 4.2 on 2023-04-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_new_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Ad')),
                ('title', models.CharField(max_length=256, verbose_name='Başlıq')),
                ('origin', models.CharField(max_length=256, verbose_name='Ad')),
                ('alcohol', models.FloatField(verbose_name='Spirt')),
                ('manifacture_year', models.IntegerField(verbose_name='Istehsal ili')),
                ('about', models.CharField(max_length=512, verbose_name='Haqqında')),
                ('composition', models.CharField(max_length=256, verbose_name='Tərkibi')),
                ('combination', models.CharField(max_length=256, verbose_name='Uygunluq')),
                ('temperature', models.CharField(max_length=256, verbose_name='Temperatur')),
                ('keeping_form', models.CharField(max_length=256, verbose_name='Saxlama forması')),
            ],
        ),
    ]

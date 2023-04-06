# Generated by Django 4.1.7 on 2023-03-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/image'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcaregory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_product_category_product_image_product_subcaregory"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-23 08:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0002_review_category_review_imageurl_review_rating_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]

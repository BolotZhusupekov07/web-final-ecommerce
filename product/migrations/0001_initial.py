# Generated by Django 3.2.4 on 2022-05-28 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "season",
                    models.CharField(
                        choices=[
                            ("весна", "Весна"),
                            ("лето", "Лето"),
                            ("осень", "Осень"),
                            ("зима", "Зима"),
                            ("школьная-форма", "Школьная-форма"),
                        ],
                        max_length=15,
                    ),
                ),
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo_1", models.ImageField(upload_to="photos/")),
                ("photo_2", models.ImageField(upload_to="photos/")),
                ("photo_3", models.ImageField(upload_to="photos/")),
                ("name", models.CharField(db_index=True, max_length=250)),
                ("description", models.TextField()),
                ("material", models.CharField(max_length=250)),
                ("age", models.CharField(max_length=250)),
                ("cost", models.DecimalField(decimal_places=1, max_digits=10)),
                ("size", models.CharField(max_length=250)),
                ("slug", models.SlugField()),
                ("hits", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        default="весна",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="product.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_cost", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]

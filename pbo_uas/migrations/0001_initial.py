# Generated by Django 5.0.4 on 2024-05-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('category_id', models.IntegerField()),
                ('image_path', models.TextField(null=True)),
                ('desc', models.TextField(null=True)),
                ('price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('desc', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'product_categories',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_no', models.CharField(max_length=32)),
                ('date', models.DateField(auto_now_add=True)),
                ('paid', models.IntegerField()),
                ('payment_method', models.CharField(default=' ', max_length=32)),
                ('change', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='SaleDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('product_category_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=64)),
                ('sold_for', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('note', models.CharField(max_length=64)),
            ],
        ),
    ]
# Generated by Django 3.0.5 on 2022-12-14 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoeshop', '0002_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='barand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shoeshop.Category'),
        ),
    ]
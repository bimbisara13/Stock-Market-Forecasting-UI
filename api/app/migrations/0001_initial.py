# Generated by Django 4.1.2 on 2022-11-30 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MLModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=20)),
                ('best_model', models.CharField(max_length=20)),
                ('mape', models.FloatField()),
            ],
        ),
    ]

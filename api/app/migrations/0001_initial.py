# Generated by Django 4.1.2 on 2022-11-13 19:28

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
                ('xgboost', models.FloatField()),
                ('random_forest', models.FloatField()),
                ('lasso', models.FloatField()),
                ('ridge', models.FloatField()),
            ],
        ),
    ]

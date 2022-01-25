# Generated by Django 3.2.7 on 2022-01-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('img_url', models.URLField()),
                ('price', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]

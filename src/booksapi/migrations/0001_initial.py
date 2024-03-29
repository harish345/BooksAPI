# Generated by Django 2.2.2 on 2019-06-30 07:57

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('isbn', models.CharField(max_length=256)),
                ('authors', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=128, size=None)),
                ('country', models.CharField(max_length=128)),
                ('number_of_pages', models.IntegerField()),
                ('publisher', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]

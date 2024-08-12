# Generated by Django 4.2.4 on 2023-09-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomModel',
            fields=[
                ('name', models.CharField(max_length=255, unique=True)),
                ('_password', models.CharField(db_column='password', max_length=255)),
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'unique_together': {('name', '_password')},
            },
        ),
    ]

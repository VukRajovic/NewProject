# Generated by Django 3.1.5 on 2021-01-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
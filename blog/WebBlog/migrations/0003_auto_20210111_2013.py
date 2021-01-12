# Generated by Django 3.1.5 on 2021-01-11 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebBlog', '0002_auto_20210111_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='EmployeeId',
            new_name='employeeId',
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
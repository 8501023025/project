# Generated by Django 3.2.9 on 2021-12-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-26 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210126_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
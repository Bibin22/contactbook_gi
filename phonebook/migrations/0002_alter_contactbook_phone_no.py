# Generated by Django 4.1.2 on 2022-10-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactbook',
            name='phone_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]

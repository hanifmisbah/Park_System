# Generated by Django 3.2.3 on 2021-10-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiket', '0007_auto_20211031_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='noblok',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3')], default='', max_length=3),
        ),
    ]
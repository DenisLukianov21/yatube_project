# Generated by Django 2.2.19 on 2022-08-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220818_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='adress',
            field=models.SlugField(),
        ),
    ]
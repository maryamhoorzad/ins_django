# Generated by Django 2.0.5 on 2019-07-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='store.Category'),
        ),
    ]

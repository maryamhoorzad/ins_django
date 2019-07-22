# Generated by Django 2.0.5 on 2019-07-06 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.TextField()),
                ('persian_name', models.TextField()),
                ('brand_desc', models.TextField()),
                ('picture', models.FileField(upload_to='static/product_pics/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('picture', models.FileField(upload_to='static/product_pics/')),
                ('parent', models.ManyToManyField(blank=True, null=True, related_name='_category_parent_+', to='store.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('sous_titre', models.TextField()),
                ('description', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('picture', models.FileField(upload_to='static/product_pics/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Brand')),
                ('category', models.ManyToManyField(blank=True, null=True, to='store.Category')),
            ],
        ),
    ]
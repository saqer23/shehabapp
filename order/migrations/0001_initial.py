# Generated by Django 3.2.9 on 2022-03-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=35)),
                ('category_slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]

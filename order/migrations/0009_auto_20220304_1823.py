# Generated by Django 3.2.9 on 2022-03-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_bill_bill_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderactive',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
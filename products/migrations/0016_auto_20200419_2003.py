# Generated by Django 2.2.7 on 2020-04-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20200419_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='value',
            field=models.CharField(blank=True, choices=[('1', 'Cat'), ('2', 'Dog'), ('3', 'Bird'), ('4', 'Featured'), ('5', 'Fishes'), ('0', 'Accessories')], max_length=100, null=True),
        ),
    ]

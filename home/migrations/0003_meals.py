# Generated by Django 3.2.7 on 2021-09-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_grocerries_grocerries_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meals_Image', models.ImageField(upload_to='home/images')),
                ('Meals_Name', models.CharField(max_length=50)),
                ('Meals_quantity', models.FloatField()),
                ('Meals_Price', models.FloatField()),
            ],
        ),
    ]
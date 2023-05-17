# Generated by Django 4.2.1 on 2023-05-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_drinkscategory_drinks_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('reservation_time', models.DateField(auto_now=True)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-24 13:13

import django.db.models.deletion
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
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/blog')),
                ('title', models.CharField(max_length=100)),
                ('create_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myportfolio.category')),
            ],
        ),
    ]

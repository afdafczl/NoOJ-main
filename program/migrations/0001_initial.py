# Generated by Django 4.1.5 on 2023-03-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('Program_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Program_giturl', models.CharField(max_length=100)),
            ],
        ),
    ]

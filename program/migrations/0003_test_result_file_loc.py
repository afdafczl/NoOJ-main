# Generated by Django 4.1.5 on 2023-03-29 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_program_user_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='result_file_loc',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
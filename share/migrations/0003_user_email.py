# Generated by Django 3.1.3 on 2021-02-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_auto_20210216_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
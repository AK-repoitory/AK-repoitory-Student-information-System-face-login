# Generated by Django 3.0.6 on 2020-05-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='email',
            field=models.EmailField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='marks',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='marks',
            name='last_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='marks',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]

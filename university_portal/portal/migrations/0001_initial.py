# Generated by Django 3.0.6 on 2020-05-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('croll', models.IntegerField(max_length=7, primary_key=True, serialize=False)),
                ('cname', models.CharField(default='', max_length=20)),
                ('cemail', models.EmailField(default='', max_length=20)),
                ('query', models.TextField()),
            ],
        ),
    ]

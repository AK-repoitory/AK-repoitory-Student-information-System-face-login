# Generated by Django 3.0.6 on 2020-05-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20200515_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]

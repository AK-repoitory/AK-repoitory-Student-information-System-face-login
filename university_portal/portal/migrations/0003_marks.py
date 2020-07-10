# Generated by Django 3.0.6 on 2020-05-14 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0002_auto_20200514_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField(default=0)),
                ('Subject_Networking', models.FloatField(default=0)),
                ('Subject_java', models.FloatField(default=0)),
                ('Subject_c', models.FloatField(default=0)),
                ('Subject_python', models.FloatField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
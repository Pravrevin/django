# Generated by Django 2.2 on 2019-12-22 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('refercode', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 3.0.dev20190625091245 on 2019-06-27 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
    ]

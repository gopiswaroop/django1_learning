# Generated by Django 3.1.7 on 2021-03-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('fathername', models.CharField(max_length=1000)),
                ('classname', models.IntegerField()),
                ('contact', models.CharField(max_length=1000)),
            ],
        ),
    ]

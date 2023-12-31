# Generated by Django 4.2.2 on 2023-08-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='film',
            fields=[
                ('movie_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('yearRelease', models.DateField()),
                ('rating', models.IntegerField()),
                ('path', models.CharField(max_length=250)),
                ('filmType', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='netflixUsers',
            fields=[
                ('user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=220)),
                ('lname', models.CharField(max_length=220)),
                ('email', models.CharField(max_length=220)),
                ('dob', models.DateField()),
            ],
        ),
    ]

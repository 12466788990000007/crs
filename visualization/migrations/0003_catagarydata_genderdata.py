# Generated by Django 2.0 on 2022-06-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0002_auto_20220614_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='catagaryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depatment', models.CharField(max_length=100)),
                ('totalstu4', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Catagorieswise placed Student Data',
            },
        ),
        migrations.CreateModel(
            name='GenderData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
                ('totalstu3', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Genderwise placed Student Data',
            },
        ),
    ]

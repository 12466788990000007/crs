# Generated by Django 2.0 on 2022-06-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0003_catagarydata_genderdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnplacedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Placedunplaced', models.CharField(max_length=100)),
                ('totalstu5', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'placementwise placed -unplaced Student Data',
            },
        ),
    ]

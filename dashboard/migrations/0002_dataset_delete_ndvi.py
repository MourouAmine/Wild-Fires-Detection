# Generated by Django 5.0.3 on 2024-04-22 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ndvi', models.FloatField()),
                ('lst', models.FloatField()),
                ('burned_area', models.FloatField()),
                ('classification', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('month', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='ndvi',
        ),
    ]

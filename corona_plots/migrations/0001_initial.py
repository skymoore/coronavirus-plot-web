# Generated by Django 3.0.4 on 2020-03-22 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_state', models.CharField(default='', max_length=100)),
                ('region_country', models.CharField(default='', max_length=100)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('friendly_name', models.CharField(max_length=100)),
                ('friendly_hash', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('count', models.IntegerField(default=0)),
                ('case_status_type_id', models.CharField(max_length=25)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corona_plots.Location')),
            ],
        ),
    ]

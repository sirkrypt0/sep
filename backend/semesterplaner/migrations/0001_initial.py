# Generated by Django 3.0.3 on 2020-03-03 22:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('lp', models.IntegerField(default=6)),
                ('semester', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=1)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday')], default=0)),
                ('time', models.TimeField(choices=[(datetime.time(9, 0), '9:00'), (datetime.time(9, 15), '9:15'), (datetime.time(11, 0), '11:00'), (datetime.time(13, 30), '13:30'), (datetime.time(15, 15), '15:15'), (datetime.time(17, 0), '17:00')], verbose_name='Starting time')),
                ('hall', models.CharField(default='HS 1', max_length=20)),
                ('type', models.IntegerField(choices=[(0, 'Lecture'), (1, 'Exercise')], default=0)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semesterplaner.Lecture')),
                ('duration', models.IntegerField(choices=[(45, 45), (90, 90), (135, 135), (180, 180), (225, 225), (270, 270), (315, 315), (360, 360)], default=90))
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semesterplaner.Lecturer'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-22 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('lp', models.IntegerField(default=6)),
                ('semester', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=1)),
                ('hall', models.CharField(default='HS 1', max_length=20)),
                ('description', models.TextField()),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semesterplaner.Lecturer')),
            ],
        ),
    ]
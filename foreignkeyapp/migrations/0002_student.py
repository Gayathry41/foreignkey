# Generated by Django 5.0.6 on 2024-07-22 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreignkeyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_address', models.CharField(max_length=200)),
                ('student_age', models.IntegerField(blank=True, null=True)),
                ('joining_date', models.DateField(null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foreignkeyapp.course')),
            ],
        ),
    ]

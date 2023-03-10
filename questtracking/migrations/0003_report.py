# Generated by Django 4.0.7 on 2023-02-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questtracking', '0002_projectmodel_batch_projectmodel_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Projectname', models.CharField(max_length=50)),
                ('Teamname', models.CharField(max_length=50)),
                ('Analysis', models.CharField(max_length=50)),
                ('Design', models.CharField(max_length=50)),
                ('Development', models.CharField(max_length=50)),
                ('Testing', models.CharField(max_length=50)),
                ('Documentation', models.CharField(max_length=50)),
            ],
        ),
    ]
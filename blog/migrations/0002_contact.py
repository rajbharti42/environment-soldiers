# Generated by Django 3.2.4 on 2021-07-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50000)),
            ],
        ),
    ]

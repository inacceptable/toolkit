# Generated by Django 3.2.8 on 2022-03-10 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('suggestion', models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.2.12 on 2022-05-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mtt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('imgs', models.ImageField(upload_to='pics')),
                ('detail', models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-04-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

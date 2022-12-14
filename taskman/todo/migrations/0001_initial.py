# Generated by Django 4.1.2 on 2022-10-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('created_on', models.DateField(auto_now=True)),
                ('complete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]

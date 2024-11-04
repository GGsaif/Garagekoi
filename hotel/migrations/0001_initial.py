# Generated by Django 4.0.5 on 2022-07-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('category', models.CharField(choices=[('P', 'premium'), ('D', 'deluxe'), ('B', 'basic'), ('Q', 'Queen'), ('Q', 'King')], max_length=3)),
                ('beds', models.IntegerField(default=1)),
                ('capacity', models.IntegerField(default=1)),
            ],
        ),
    ]
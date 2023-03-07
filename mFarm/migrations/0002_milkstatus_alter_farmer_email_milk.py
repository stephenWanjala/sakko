# Generated by Django 4.1.7 on 2023-03-07 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mFarm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilkStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fresh', models.BooleanField(default=True)),
                ('spoilt', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='farmer',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.CreateModel(
            name='Milk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mFarm.farmer')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mFarm.milkstatus')),
            ],
        ),
    ]

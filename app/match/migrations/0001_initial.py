# Generated by Django 3.2.7 on 2021-09-17 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('first_name', models.CharField(max_length=10)),
                ('second_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.gender')),
            ],
        ),
    ]
# Generated by Django 3.2.4 on 2021-06-02 20:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Female', max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Female', max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('nickname', models.CharField(max_length=50)),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contactbook.contact')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
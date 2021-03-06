# Generated by Django 2.1.5 on 2019-03-14 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ac_login', '0001_initial'),
        ('ac_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenRegister',
            fields=[
                ('ctid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='citizen/')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_login.Login')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('image', models.ImageField(upload_to='complaints/')),
                ('registerdate', models.DateField()),
                ('status', models.CharField(max_length=10)),
                ('closedate', models.DateField()),
                ('ctid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_citizen.CitizenRegister')),
                ('department', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='ac_admin.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Feeback',
            fields=[
                ('fid', models.IntegerField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('image', models.ImageField(upload_to='feedback/')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_citizen.Complaint')),
                ('ctid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_citizen.CitizenRegister')),
            ],
        ),
    ]

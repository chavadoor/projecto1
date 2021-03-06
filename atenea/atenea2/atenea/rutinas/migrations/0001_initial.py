# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 05:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=100)),
                ('foto', django_resized.forms.ResizedImageField(crop=['middle', 'center'], keep_meta=True, quality=75, size=[450, 350], upload_to='media/img')),
            ],
        ),
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('rutina', models.FileField(upload_to='files/pdf')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutinas.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('sucursal', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='rutina',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutinas.Sexo'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutinas.Sucursal'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-11 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('documento', models.CharField(max_length=15)),
                ('profissao', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=255)),
                ('rua', models.CharField(max_length=255)),
                ('complemento', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=255)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='importer_export.cliente')),
            ],
        ),
    ]
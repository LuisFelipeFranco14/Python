# Generated by Django 5.0.4 on 2024-04-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_variacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]

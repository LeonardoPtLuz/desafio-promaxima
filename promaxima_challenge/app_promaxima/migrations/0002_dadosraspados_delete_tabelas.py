# Generated by Django 5.0.2 on 2024-03-04 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_promaxima', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosRaspados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto', models.CharField(max_length=255)),
                ('modalidade', models.CharField(max_length=100)),
                ('comprador', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('unidade', models.CharField(max_length=50)),
                ('quantidade', models.CharField(max_length=50)),
                ('valor', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Tabelas',
        ),
    ]

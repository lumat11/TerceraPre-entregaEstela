# Generated by Django 4.2.7 on 2023-11-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTerceraEntrega', '0002_rename_equipo_futbol_equipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadio', models.CharField(default='ValorPorDefecto', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=30)),
                ('continente', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='nombre',
        ),
        migrations.AddField(
            model_name='equipo',
            name='equipo',
            field=models.CharField(default='ValorPorDefecto', max_length=30),
        ),
        migrations.AddField(
            model_name='equipo',
            name='liga',
            field=models.CharField(default='ValorPorDefecto', max_length=30),
        ),
    ]

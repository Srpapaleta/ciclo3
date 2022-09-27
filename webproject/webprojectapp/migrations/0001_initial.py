# Generated by Django 4.1 on 2022-09-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula_inmueble', models.TextField()),
                ('ciudad', models.TextField()),
                ('direccion', models.CharField(max_length=50)),
                ('nombre_unidad_residencial', models.CharField(max_length=250)),
                ('numero_piso', models.IntegerField()),
                ('numero_apartamento', models.IntegerField()),
                ('numero_habitaciones', models.IntegerField()),
                ('numero_banos', models.IntegerField()),
                ('tiene_piscina', models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], default='NO', max_length=2)),
                ('precio_dia', models.TextField()),
            ],
        ),
    ]
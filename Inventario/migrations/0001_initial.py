from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_producto', models.CharField(max_length=30, verbose_name='CÓDIGO PRODUCTO')),
                ('descripcion', models.CharField(max_length=100, verbose_name='DESCRIPCIÓN')),
                ('existencias', models.PositiveSmallIntegerField(verbose_name='EXISTENCIAS')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PRECIO')),
                ('suma', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='SUMA')),
            ],
        ),
    ]

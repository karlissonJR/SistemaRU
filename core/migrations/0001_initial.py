# Generated by Django 2.2.6 on 2019-11-21 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumidor',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=100)),
                ('credito', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('bolsista', models.BooleanField(default=False)),
                ('modalidade', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=100)),
                ('funcao', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_hora', models.DateTimeField(verbose_name='data da transação')),
            ],
        ),
        migrations.CreateModel(
            name='GRU',
            fields=[
                ('codigo_barras', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nome_computador', models.CharField(max_length=50)),
                ('competencia', models.CharField(max_length=50)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Funcionario')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-11 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividades',
            name='id_turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sistema.turma', verbose_name='Id-Turma'),
        ),
    ]

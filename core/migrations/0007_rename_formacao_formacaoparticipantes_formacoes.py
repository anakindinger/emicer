# Generated by Django 4.0.6 on 2022-08-04 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_participante_formacoes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formacaoparticipantes',
            old_name='formacao',
            new_name='formacoes',
        ),
    ]

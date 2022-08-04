# Generated by Django 4.0.6 on 2022-08-04 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_participante_formacao_participantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormacaoParticipantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='formacao',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='formacao',
            name='duracao',
            field=models.DurationField(verbose_name='Duração'),
        ),
        migrations.AlterField(
            model_name='formacao',
            name='participantes',
            field=models.ManyToManyField(through='core.FormacaoParticipantes', to='core.participante'),
        ),
        migrations.AddField(
            model_name='formacaoparticipantes',
            name='formacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.formacao'),
        ),
        migrations.AddField(
            model_name='formacaoparticipantes',
            name='participantes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.participante'),
        ),
    ]
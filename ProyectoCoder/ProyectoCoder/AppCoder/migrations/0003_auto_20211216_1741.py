# Generated by Django 3.2.9 on 2021-12-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_jugador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('celular', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Curso',
            new_name='Rescatados',
        ),
        migrations.DeleteModel(
            name='Jugador',
        ),
        migrations.RenameField(
            model_name='rescatados',
            old_name='camada',
            new_name='edad',
        ),
    ]
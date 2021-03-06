# Generated by Django 3.2.4 on 2021-06-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=255)),
                ('nascimento', models.DateField()),
                ('idade', models.IntegerField(max_length=3)),
                ('cpf', models.CharField(db_index=True, max_length=14)),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=15)),
                ('bairro', models.CharField(max_length=255)),
            ],
        ),
    ]

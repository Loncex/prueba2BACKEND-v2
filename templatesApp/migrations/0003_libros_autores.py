# Generated by Django 4.2.6 on 2023-11-20 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatesApp', '0002_alter_autor_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='libros',
            name='autores',
            field=models.ManyToManyField(to='templatesApp.autor'),
        ),
    ]
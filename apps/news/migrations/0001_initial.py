# Generated by Django 2.2.13 on 2021-02-20 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, verbose_name='Sexo')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('curriculo', models.TextField(verbose_name='Currículo')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'Autor',
                'ordering': ['nome'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('data_publicacao', models.DateField(verbose_name='Data da Publicação')),
                ('categoria', models.CharField(choices=[('IN', 'INFORMÁTICA'), ('PR', 'PROGRAMAÇÃO'), ('IO', 'INTERNET DAS COISAS'), ('BD', 'BANCO DE DADOS')], max_length=2, verbose_name='Categoria')),
                ('assunto', models.CharField(max_length=150, verbose_name='Assunto')),
                ('foto_publicacao', models.ImageField(blank=True, null=True, upload_to='fotos_publicacoes', verbose_name='Foto Publicação')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Autor')),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
                'db_table': 'Noticia',
                'ordering': ['-data_publicacao', 'categoria'],
                'managed': True,
            },
        ),
    ]

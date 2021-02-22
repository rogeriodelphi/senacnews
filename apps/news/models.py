from django.db import models

class Autor(models.Model):
    SEXO_CHOICES  = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    nome = models.CharField('Nome', max_length=150)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)
    idade = models.IntegerField('Idade')
    cidade = models.CharField('Cidade', max_length=150)
    curriculo = models.TextField('Currículo')

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'Autor'
        ordering = ['nome']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Noticia(models.Model):
    CATEGORIA_CHOICES = [
        ('IN', 'INFORMÁTICA'),
        ('PR', 'PROGRAMAÇÃO'),
        ('IO', 'INTERNET DAS COISAS'),
        ('BD', 'BANCO DE DADOS'),
    ]
    titulo = models.CharField('Titulo', max_length=150)
    texto = models.TextField('Texto')
    data_publicacao= models.DateTimeField(auto_now_add=True)
    categoria = models.CharField('Categoria', max_length=2, choices=CATEGORIA_CHOICES)
    assunto = models.CharField('Assunto', max_length=150)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    foto_publicacao = models.ImageField('Foto Publicação', upload_to='media/images/noticias', blank=True, null=True)

    # @property
    # def photo_url(self):
    #     if self.foto_publicacao and hasattr(self.foto_publicacao, 'url'):
    #         return self.foto_publicacao.url

    def __str__(self):
        return self.titulo

    class Meta:
        managed = True
        db_table = 'Noticia'
        ordering = ['-data_publicacao', 'categoria']
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
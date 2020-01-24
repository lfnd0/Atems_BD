from django.db import models
from django.contrib.auth.models import User

class Local(models.Model):
    nome = models.CharField(max_length=100)

    class Meta():
        verbose_name_plural = 'Locais'

    def __str__(self):
        return self.nome

class Distribuidora(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='distribuidoras')
    nome = models.CharField(max_length=100)
    local = models.ManyToManyField(Local)
    
    def __str__(self):
	    return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    class Meta():
        verbose_name_plural = 'Gêneros'
    
    def __str__(self):
	    return self.nome

class ClassificacaoIndicativa(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta():
        verbose_name_plural = 'Classificação indicativa'

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data_lancamento = models.DateField()
    distribuidora = models.OneToOneField(Distribuidora, on_delete=models.CASCADE)
    genero = models.OneToOneField(Genero, on_delete=models.CASCADE)
    classificacao_indicativa = models.OneToOneField(ClassificacaoIndicativa, on_delete=models.CASCADE)

    class Meta:
        abstract = True
    
    def __str__(self):
	    return self.nome

class JogoGratuito(Jogo):

    class Meta():
        verbose_name_plural = 'Jogos gratuitos'

class JogoPago(Jogo):
    preco = models.FloatField()

    class Meta():
        verbose_name_plural = 'Jogos pagos'
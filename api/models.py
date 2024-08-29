from django.db import models

class Produto(models.Model):
    tituloProduto = models.CharField(max_length=255)

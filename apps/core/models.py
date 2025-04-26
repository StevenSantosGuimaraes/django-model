from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class CentroCusto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    centro_custo = models.ForeignKey(CentroCusto, on_delete=models.CASCADE)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class FolhaPagamento(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    competencia = models.DateField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['funcionario', 'competencia']

    def __str__(self):
        return f"{self.funcionario} - {self.competencia.strftime('%Y-%m')}"

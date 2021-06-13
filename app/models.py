from django.db import models


class Student(models.Model):

    name = models.CharField(name='nome', max_length=255, db_index=True)
    birthday = models.DateField(name='nascimento')
    age = models.IntegerField(name='idade')
    cpf = models.CharField(name='cpf', max_length=14, db_index=True)
    street = models.CharField(name='rua', max_length=255)
    number = models.CharField(name='numero', max_length=10)
    complement = models.CharField(name='complemento', max_length=15)
    distric = models.CharField(name='bairro', max_length=255)
    


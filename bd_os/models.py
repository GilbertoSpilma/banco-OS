from django.db import models

class NFE(models.Model):
    NFE = models.IntegerField()
    
    def __str__(self):
        return self.NFE

class STATUS(models.Model):
    STATUS = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.STATUS

class TECNICO(models.Model):
    TECNICO = models.CharField(max_length=255)
    
    def __str__(self):
        return self.TECNICO

class NFS(models.Model):
    NFS = models.IntegerField()
    
    def __str__(self):
        return self.NFS

class CLIENTE(models.Model):
    CLIENTE = models.CharField(max_length=255)
    
    def __str__(self):
        return self.CLIENTE

class MARCA(models.Model):
    MARCA = models.CharField(max_length=255)
    
    def __str__(self):
        return self.MARCA

class EQUIPAMENTO(models.Model):
    EQUIPAMENTO = models.CharField(max_length=255)
    MARCA= models.ForeignKey(MARCA, on_delete=models.PROTECT, default=1)
    def __str__(self):
        return self.EQUIPAMENTO


class OS(models.Model):
    DATA_ENTRADA =  models.DateField(null=True, blank=True)
    DATA_SAIDA = models.DateField(null=True, blank=True)
    DEFEITO_INFORMADO = models.TextField(null=True, blank=True)
    EQUIPAMENTO=models.ForeignKey(EQUIPAMENTO,on_delete=models.PROTECT, default=1)
    NUMERO_SERIE=models.IntegerField(null=True, blank=True)
    NUMERO_ORÇAMENTO=models.IntegerField(null=True, blank=True)
    DESCRIÇÃO_REPARO= models.TextField(null=True, blank=True) 
    CLIENTE = models.ForeignKey(CLIENTE, on_delete=models.PROTECT, default=1)
    STATUS=models.ForeignKey( STATUS,on_delete=models.PROTECT, default=1)
    TECNICO=models.ForeignKey(TECNICO,on_delete=models.PROTECT, default=1)
    NFE=models.IntegerField(null=True, blank=True)
    NFS=models.IntegerField(null=True, blank=True)  

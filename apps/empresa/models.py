from turtle import mode
from django.db import models

# Create your models here.

class Business(models.Model):
    name = models.CharField(verbose_name='Negocio', max_length=50, blank=False)
    direction = models.CharField(verbose_name='Dirección', max_length=50, blank=False)
    ruc = models.IntegerField(verbose_name='RUC', blank=True)
    history = models.TextField(verbose_name='Historia', blank=True)
    vision = models.TextField(verbose_name='visión', blank=False)
    mision = models.TextField(verbose_name='mision', blank=False)
    image = models.ImageField(verbose_name='imagen', upload_to='empresa', blank=False)
    status = models.BooleanField(verbose_name='Estado', help_text='Alta/Baja', default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'

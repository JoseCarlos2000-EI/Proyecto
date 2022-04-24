from turtle import mode
from unicodedata import name
from django.db import models
from apps.categoria.models import Categoria
from apps.empresa.models import Business

# Create your models here.

class Producto(models.Model):
    business = models.ForeignKey(Business,verbose_name='Empresa', blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Categoria, verbose_name='Categoría', blank=False, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nombre', max_length=50, blank=False)
    description = models.TextField(verbose_name='Descripción', blank=True)
    price = models.DecimalField(verbose_name='Precio', max_digits=5, decimal_places=2, blank=False)
    stock = models.IntegerField(verbose_name='Stock', blank=False)
    image1 = models.ImageField(verbose_name='Imagen 1', upload_to='producto', blank=False)
    image2 = models.ImageField(verbose_name='Imagen 2', upload_to='producto', blank=False)
    image3 = models.ImageField(verbose_name='Imagen 3', upload_to='producto', blank=False)
    image4 = models.ImageField(verbose_name='Imagen 4', upload_to='producto', blank=False)
    status = models.BooleanField(verbose_name='Estado', help_text='Alta/Baja', default=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural ='Productos'
        ordering = ('id',)

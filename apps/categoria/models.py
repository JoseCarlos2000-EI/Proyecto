from django.db import models
from apps.empresa.models import Business

# Create your models here.
class Categoria (models.Model):
    business = models.ForeignKey(Business,verbose_name='Empresa', blank=False, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Categoría', max_length=50, blank=False)
    description = models.TextField(verbose_name='Descripción', blank=False)
    image = models.ImageField(verbose_name='Imagen', upload_to='categoria', blank=False)
    status = models.BooleanField(verbose_name='estado', help_text='Alta/Baja', default=True)

    def __str__(self):
        return '{}-{}'.format(self.name, self.business)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural ='Categorías'
        ordering = ('id',)


from django.db import models

from django.utils.safestring import mark_safe
# Create your models here.
class BigParent(models.Model):
    magacDhamaysiran=models.CharField(max_length=255)
    faahfaahin=models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        return str(self.magacDhamaysiran)


class Parent(models.Model):
    waalidka=models.ForeignKey(BigParent,on_delete=models.CASCADE,default=1)
    magacDhamaysiran=models.CharField(max_length=255)
    sawirka=models.ImageField(upload_to='sawirada/waalidinta',null=True,blank=True)
    magacKuGalid=models.CharField(max_length=255)
    number=models.CharField(max_length=255)
    tiradaXaasaska=models.IntegerField(default=3)
    password=models.CharField(max_length=255)
    faahfaahin=models.TextField(null=True,blank=True)

    def pSawirka(self):
        if self.sawirka:
            return mark_safe('<img src={} width="100px" >'.format(self.sawirka.url))
        else:
            return mark_safe('<img src={} width="100px" >'.format('https://st3.depositphotos.com/3581215/18899/v/450/depositphotos_188994514-stock-illustration-vector-illustration-male-silhouette-profile.jpg')) 
    pSawirka.allow_tags=True
    def __str__(self) -> str:
        return str(self.magacDhamaysiran)
JINSIGA = (
    ('wiil','WIIL'),
    ('gabar', 'GABAR')
)


class PChild(models.Model):
    waalidka=models.ForeignKey(Parent,on_delete=models.CASCADE,default=1)
    magacDhamaysiran=models.CharField(max_length=255)
    sawirka=models.ImageField(upload_to='sawirada/waalidinta',null=True,blank=True)
    magacaHooyada=models.CharField(max_length=255)
    magacKuGalid=models.CharField(max_length=255)
    jinsiga=models.CharField(max_length=255,choices=JINSIGA,default='wiil')
    number=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    faahfaahin=models.TextField(null=True,blank=True)

    def cSawirka(self):
        if self.sawirka:
            return mark_safe('<img src={} width="100px" >'.format(self.sawirka.url))
        else:
            return mark_safe('<img src={} width="100px" >'.format('https://st3.depositphotos.com/3581215/18899/v/450/depositphotos_188994514-stock-illustration-vector-illustration-male-silhouette-profile.jpg')) 
    cSawirka.allow_tags=True

    def __str__(self) -> str:
        return str(self.magacDhamaysiran)
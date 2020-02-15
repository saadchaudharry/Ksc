from django.db import models
from django.urls import reverse

# Create your models here.

class Catagory(models.Model):
    image =models.ImageField()
    name  =models.CharField(max_length=100)
    slug  =models.SlugField(max_length=100)

    class Meta:
        verbose_name='catagory'
        verbose_name_plural='catagories'

    def get_absoulte_url(self):
        return reverse('post:list_of_catagory',args=[self.slug])

    def __str__(self):
        return str(self.name)

class Prod(models.Model):
    image       =models.ImageField()
    name        =models.CharField(max_length=100)
    price       =models.IntegerField()
    catagory    =models.ForeignKey(Catagory,on_delete=models.CASCADE)
    description =models.TextField(max_length=12000)
    status      =models.CharField(max_length=12000,default='publish')
    def __str__(self):
        return str(self.name)


class Contactus(models.Model):
    Name     =models.CharField(max_length=120)
    Email    =models.CharField(max_length=120)
    Phone    =models.IntegerField()
    Message  =models.TextField(max_length=1200)

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name='contactform'
        verbose_name_plural='contact'

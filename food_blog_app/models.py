from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Food_Post(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'Food Title')
    slug = models.SlugField(max_length=120,unique=True,verbose_name='Food Slug')
    text = models.TextField(verbose_name='About Food')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    publish = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')


    class Meta:
        verbose_name = 'Food Post'
        verbose_name_plural = 'Food Posts'

    def __str__(self):
        return str(self.title)


    
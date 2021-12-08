from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=500)
    slug= models.SlugField(unique=True)
    body= models.TextField()
    image=models.ImageField(upload_to='images',null=True,blank=True)

    def __str__(self):
        return f'{self.title}- {self.slug}'
        
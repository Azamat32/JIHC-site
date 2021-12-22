from django.db import models
from django.views.generic import ListView, DetailView
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import RegexValidator,FileExtensionValidator
# Create your models here.
from unidecode import unidecode


class SwiperImg(models.Model):

    img = models.ImageField(upload_to="gallery")


class Post(models.Model):
    class Meta:
        abstract = True
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=400)
    img = models.ImageField(upload_to="gallery")
    
    def __str__(self):
        return(self.title)

class TalapkerPost(Post):

    
    def __str__(self):
        return " {} ".format(self.title)

class NewsLongPost(Post):
    
 def __str__(self):
        return " {} ".format(self.title)

class NewsBigPost(Post):
    
 def __str__(self):
        return " {} ".format(self.title)

class NewsShortPost(Post):
    def __str__(self):
        return " {} ".format(self.title)



class NavList(models.Model):
    title = models.CharField(max_length=20 , default='')
    slug = models.SlugField(default='',unique=True)
    description = models.TextField(max_length=600,default='',verbose_name=' Первый абзац')
    description_second = models.TextField(max_length=600,default='',verbose_name=' Второй абзац')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NavList, self).save(*args, **kwargs)
    def __str__(self):
        return " {} ".format(self.title)
    




class NewsPostForm(models.Model):

    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="gallery")
    date = models.DateField()
    slug = models.SlugField(default='',unique=True)
    
    description = models.TextField(max_length=900)
    def __str__(self):
        return " {} ".format(self.title)
  
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(NewsPostForm, self).save(*args, **kwargs)


class Gallery(models.Model):
    img = models.ImageField(upload_to="gallery" )

    title = models.CharField(max_length=20,default='')


class TalapkerPageTable(models.Model):
    title = models.CharField(max_length=20 ,default='')
    number = models.CharField(primary_key=True, max_length=6, validators=[RegexValidator(r'^\d{1,6}$')])
    table_description = models.TextField(max_length=50)
    date = models.CharField(max_length=20)
    def __str__(self):
        return(self.title)
    


class StudentPageForm(models.Model):
   
    title = models.CharField(max_length=20 ,default='')
    video = models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    video_descriptions = models.TextField(max_length=255 ,default= '')
    description = models.TextField(max_length=255,verbose_name=' Первый абзац')
    description_second = models.TextField(max_length=255,verbose_name=' Второй абзац',default='')
    def __str__(self):
        return(self.title)
   



    
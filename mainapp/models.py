from django.db import models
from django.views.generic import ListView, DetailView
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import RegexValidator,FileExtensionValidator
# Create your models here.
from unidecode import unidecode



class SwiperImg(models.Model):

    img = models.ImageField(upload_to="gallery")
    description = models.TextField(max_length=100,default='')
class SwiperVideo(models.Model):
    video = models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])



class Post(models.Model):
    class Meta:
        abstract = True
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=400)
    img = models.ImageField(upload_to="gallery")
    descriptionRU = models.TextField(max_length=400,default='')
    descriptionEN = models.TextField(max_length=400,default='')
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
    description = models.TextField(max_length=800,default='',verbose_name=' Первый абзац ')
    
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
    
    description = models.TextField(max_length=900,default='')
    


    def __str__(self):
        return " {} ".format(self.title)
  
    def save(self, *args, **kwargs):
        super(NewsPostForm, self).save(*args, **kwargs)


class Gallery(models.Model):
    img = models.ImageField(upload_to="gallery" )

    title = models.CharField(max_length=20,default='')
    def __str__(self):
        return " {} ".format(self.title)

class TalapkerPageTable(models.Model):
    title = models.CharField(max_length=20 ,default='')
    number = models.CharField(primary_key=True, max_length=6, validators=[RegexValidator(r'^\d{1,6}$')])
    table_description = models.TextField(max_length=100,verbose_name = 'Мамандык туралы')
    table_description2 = models.TextField(max_length=100,default='',verbose_name = 'Біліктілік туралы')    
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


class students_life_img(models.Model):

    img = models.ImageField(upload_to="gallery")
    
class students_life_description(models.Model):
    
    description = models.TextField(max_length=600,default='')

class clubs_page_form(models.Model):

    title = models.CharField(max_length=20 , default='')
    club_description = models.TextField(max_length=500,default='')
    image = models.FileField(blank=True)
    
    def __str__(self):
        return (self.title)

class clubs_page_video(models.Model):
    video = models.FileField(upload_to='videos_uploaded',verbose_name='Основной плеер страницы',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    

class clubImage(models.Model):
    club = models.ForeignKey(clubs_page_form,default=None,on_delete=models.CASCADE)
    image = models.FileField(upload_to = 'gallery')
 
class For_parents(models.Model):

    title = models.CharField(max_length=40)
    description = models.TextField(max_length=500)


    def __str__(self):

        return (self.title)

class ValounterVideo(models.Model):

    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos_uploaded',verbose_name='Основной плеер страницы',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    def __str__(self):
        return (self.title)



    
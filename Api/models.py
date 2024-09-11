from django.db import models

# Create your models here.
class Testimonal(models.Model):
    name = models.CharField(max_length=50)
    campany=models.CharField(max_length=50)
    image=models.ImageField(upload_to="Testimonals/")
    feedback=models.TextField()

class About(models.Model):
    title =models.CharField(max_length=100)
    description =models.TextField()
    image = models.ImageField(upload_to="about/")

class Brand(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Brands/')

class Contact(models.Model):
    name =models.CharField(max_length=50)
    email=models.EmailField()
    message =models.CharField(max_length=50)

class Work(models.Model):
    title = models.CharField(max_length=50)
    description= models.CharField(max_length=50)
    projectLink=models.URLField(max_length=250)
    codeLink=models.URLField(max_length=250)
    image = models.ImageField(upload_to="work/")
    tags = models.CharField(max_length=50,choices=(("UI/UX design","UI/UX design"),("Eccomerce","Eccomerce"),("Social Apps","Social Apps") ) )

class WorkExperience(models.Model):
    name=models.CharField(max_length=50)
    campany=models.CharField(max_length=50)
    desc = models.CharField(max_length=50)

class Experience(models.Model):
    year =models.CharField(max_length=25)
    works= models.ManyToManyField(WorkExperience)

class Skill(models.Model):
    name=models.CharField(max_length=50)
    bgColor=models.CharField(max_length=50,blank=True)
    icon = models.ImageField(upload_to="Skills/")
from django.db import models

class Home(models.Model):
    name = models.CharField(max_length=100)                                       
    role = models.CharField(max_length=100)                                      
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)         
    resume = models.FileField(upload_to='resume/', blank=True, null=True)          

    def __str__(self):
        return r"{self.name}"






class About(models.Model):
    heading = models.CharField(max_length=200, default="About Me")
    content = models.TextField()
    skills_heading = models.CharField(max_length=200, default="My Skills")   


    def __str__(self):
        return f" {self.heading} "

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title



class ContactInfo(models.Model):
    heading = models.CharField(max_length=200, default="Contact Me")
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.heading

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    # content = models.TextField()
    content = RichTextField(blank=True , null=True)
    headingimg = models.ImageField(upload_to='images',default="")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address= models.CharField(max_length=150)
    email = models.CharField(max_length=50)
    message = models.TextField()


    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django_currentuser.db.models import CurrentUserField
# Create your models here.

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

#class producto, este va a detallar las especificaciones del producto
#debe usarse tambien en caso de añadir como de mostrar en pantalla
#debe de tener nombre, descripcion, precio, imagen y categoria

class Product(models.Model):
    
    class Meta:
        verbose_name_plural = 'Product Profiles'
        verbose_name = 'Product'
        
    ordering = ["category"]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    details = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to="product")
    is_active = models.BooleanField(default=True)
    # category
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/product/{self.slug}"
    

# class Categories(models.Model):

#     class Meta:
#         verbose_name_plural = 'Media Files'
#         verbose_name = 'Media'
#         ordering = ["name"]
        
#     image = models.ImageField(blank=True, null=True, upload_to="media")
#     url = models.URLField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     is_image = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if self.url:
#             self.is_image = False
#         super(Media, self).save(*args, **kwargs)
#     def __str__(self):
#         return self.name